import json
from tempfile import NamedTemporaryFile
from ProcessCollection import *
from XmlResultParser import *
import multiprocessing


class Portfolio:
    def __init__(self, filename, procedure_name, num_instances, active_instances, option_selector, cmd, extra_args):
        self.option_selector = option_selector
        self.instance_factory = InstanceFactory(cmd, filename, procedure_name, extra_args)
        self.process_collection = ProcessCollection(range(multiprocessing.cpu_count()))
        self.xml_parser = XmlResultParser()

        dynamic_args = self.select_dynamic_args(num_instances)
        self.instances = self.filter_active_instances(self.create_instances(dynamic_args), active_instances)

    def filter_active_instances(self, instances, active_ids):
        return {id: instance for id, instance in instances.items() if id in active_ids}

    def run(self):
        self.start_instances(self.instances)
        self.wait_for_termination()
        return self.collect_results(self.instances)

    def select_dynamic_args(self, num_processes):
        return self.option_selector.create_arguments(num_processes)

    def create_instances(self, dynamic_args_selection):
        instances = dict()
        for id, dynamic_args in enumerate(dynamic_args_selection):
            instances[id] = self.instance_factory.create_instance(dynamic_args)
        return instances

    def start_instances(self, instances):
        for instance in instances.values():
            instance.start(self.process_collection)

    def wait_for_termination(self):
        if self.process_collection.count_running_processes() > 0:
            self.process_collection.await_termination_of_any_process()
        self.process_collection.kill_all()
        self.process_collection.await_termination_of_all_processes()

    def collect_results(self, instances):
        instances_results = []
        for id, instance in instances.items():
            instance_results = {"id": id,
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


class InstanceFactory:
    def __init__(self, cmd, dfy_filename, procedure_name, extra_args):
        self.cmd = cmd
        self.dfy_filename = dfy_filename
        self.procedure_name = procedure_name
        self.extra_args = extra_args

    def create_instance(self, dynamic_args):
        return Instance(self.cmd, self.dfy_filename, self.procedure_name, dynamic_args, self.extra_args)


class Instance:
    def __init__(self, cmd, dfy_filename, procedure_name, dynamic_args, extra_args):
        self._output_file = NamedTemporaryFile("w+b", suffix=".out")
        self._error_file = NamedTemporaryFile("w+b", suffix=".err")
        self._xml_file = NamedTemporaryFile("r", suffix=".xml")

        proc_argument = "/proc:{}".format(procedure_name)
        static_args = [cmd, dfy_filename, proc_argument] + extra_args
        xml_argument = "/xml:{}".format(self._xml_file.name)
        self._dynamic_args = dynamic_args
        self._cmd = static_args + [xml_argument] + self._dynamic_args

    def start(self, process_collection):
        return process_collection.start_process(self._cmd, stdout=self._output_file, stderr=self._error_file)

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
