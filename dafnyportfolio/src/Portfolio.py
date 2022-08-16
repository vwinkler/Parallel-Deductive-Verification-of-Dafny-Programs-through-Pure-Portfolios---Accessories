import signal
from tempfile import NamedTemporaryFile

from ProcessCollection import *
from XmlResultParser import *


class Portfolio:
    def __init__(self, filename, procedure_name, num_instances, _, option_selector, dafny_command, timeout, cpu_queue):
        self.has_terminated_forcefully = False
        self.option_selector = option_selector
        self.dafny_instance_factory = DafnyInstanceFactory(dafny_command, filename, procedure_name, timeout)
        self.process_collection = ProcessCollection(cpu_queue)
        self.xml_parser = XmlResultParser()
        self.timeout = timeout
        self.termination_reason = "unknown"

        dynamic_args = self.select_dynamic_args(num_instances)
        self.instances = self.create_dafny_instances(dynamic_args)

    def filter_active_instances(self, instances, active_ids):
        return {id: instance for id, instance in instances.items() if id in active_ids}

    def run(self):
        assert not self.has_terminated_forcefully

        self.start_dafny_instances(self.instances)
        self._set_timeout(self.timeout)
        self.wait_for_termination()
        self._unset_timeout()
        return self.collect_results(self.instances)

    def select_dynamic_args(self, num_processes):
        return self.option_selector.create_arguments(num_processes)

    def create_dafny_instances(self, dynamic_args_selection):
        instances = dict()
        for id, dynamic_args in enumerate(dynamic_args_selection):
            instances[id] = self.dafny_instance_factory.create_dafny_instance(dynamic_args)
        return instances

    def start_dafny_instances(self, instances):
        for instance in instances.values():
            instance.start(self.process_collection)

    def wait_for_termination(self):
        while self.process_collection.count_running_processes() > 0:
            terminated_process = self.process_collection.await_termination_of_any_process()
            terminated_instance = self._find_instance_with_process(terminated_process)
            if terminated_instance is not None:
                if self._is_instance_outcome_correct(terminated_instance):
                    self.has_terminated_forcefully = True
                    self.termination_reason = "instance termination"
                    self.process_collection.kill_all()
                    self.process_collection.await_termination_of_all_processes()
        if not self.has_terminated_forcefully:
            self.termination_reason = "all instances terminated unsuccessfully"

    def _is_instance_outcome_correct(self, terminated_instance):
        is_correct = False
        try:
            parsed_xml = self.xml_parser.parse(terminated_instance.open_xml_file())
            outcome = parsed_xml["methods"][0]["outcome"]
            if outcome == "correct":
                is_correct = True
        except Exception as e:
            pass
        return is_correct

    def _find_instance_with_process(self, terminated_process):
        terminated_instance = None
        for _, instance in self.instances.items():
            if instance.get_process() == terminated_process:
                terminated_instance = instance
        return terminated_instance

    def collect_results(self, instances):
        instances_results = []
        for id, instance in instances.items():
            instance_results = {"id": id,
                                "cpu": instance.get_assigned_cpu(),
                                "cmd": instance.get_command(),
                                "diversification": instance.get_dynamic_args(),
                                "stdout": instance.open_output_file().read().splitlines(),
                                "stderr": instance.open_error_file().read().splitlines(),
                                "xml": self.try_read_xml(instance)}
            instances_results.append(instance_results)
        return instances_results

    def try_read_xml(self, instance):
        try:
            xml_results = self.xml_parser.parse(instance.open_xml_file())
        except Exception as e:
            xml_results = str(e)
        return xml_results

    def _unset_timeout(self):
        signal.alarm(0)

    def _set_timeout(self, timeout):
        def handle_timeout(signum, frame):
            self.has_terminated_forcefully = True
            self.termination_reason = "portfolio timeout"
            self.process_collection.kill_all()

        signal.signal(signal.SIGALRM, handle_timeout)
        signal.alarm(timeout)


class DafnyInstanceFactory:
    def __init__(self, dafny_command, dfy_filename, procedure_name, timeout):
        self.timeout = timeout
        self.dafny_command = dafny_command
        self.dfy_filename = dfy_filename
        self.procedure_name = procedure_name

    def create_dafny_instance(self, dynamic_args):
        return DafnyInstance(self.dafny_command, self.dfy_filename, self.procedure_name, dynamic_args, self.timeout)


class DafnyInstance:
    def __init__(self, dafny_command, dfy_filename, procedure_name, dynamic_args, timeout):
        self._process = None
        self._output_file = NamedTemporaryFile("w+b", suffix=".out")
        self._error_file = NamedTemporaryFile("w+b", suffix=".err")
        self._xml_file = NamedTemporaryFile("r", suffix=".xml")

        proc_argument = "/proc:{}".format(procedure_name)
        compile_0_argument = "/compile:0"
        rlimit_argument = "/rlimit:0"
        static_args = [dafny_command, dfy_filename, proc_argument, compile_0_argument, rlimit_argument]
        xml_argument = "/xml:{}".format(self._xml_file.name)
        self._dynamic_args = dynamic_args
        self._cmd = static_args + [xml_argument] + self._dynamic_args

    def start(self, process_collection):
        self._process = process_collection.start_process(self._cmd, stdout=self._output_file, stderr=self._error_file)

    def get_command(self):
        return self._cmd

    def get_dynamic_args(self):
        return self._dynamic_args

    def open_xml_file(self):
        return open(self._xml_file.name, "rb")

    def open_output_file(self):
        return open(self._output_file.name, "rb")

    def open_error_file(self):
        return open(self._error_file.name, "rb")

    def get_assigned_cpu(self):
        return self._process.get_assigned_cpu() if self._process is not None else None

    def get_process(self):
        return self._process
