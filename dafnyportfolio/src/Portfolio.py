import json
from tempfile import NamedTemporaryFile
from ProcessCollection import *
from XmlResultParser import *


class Portfolio:
    def __init__(self, filename, procedure_name, num_processes, option_selector, dafny_command):
        self.option_selector = option_selector
        self.num_processes = num_processes
        self.filename = filename
        self.procedure_name = procedure_name
        self.dafny_command = dafny_command
        self.process_collection = ProcessCollection()

    def run(self):
        proc_argument = "/proc:*{}".format(self.procedure_name)

        dynamic_args_selection = self.option_selector.create_arguments(self.num_processes)
        cmds = dict()
        xml_files = [NamedTemporaryFile("r", suffix=".xml") for i in range(self.num_processes)]
        for id in range(self.num_processes):
            static_args = [self.dafny_command, self.filename, proc_argument, "/xml:{}".format(xml_files[id].name)]
            dynamic_args = dynamic_args_selection[id]
            cmds[id] = static_args + dynamic_args
            self.process_collection.start_process(cmds[id])

        while self.process_collection.count_running_processes() > 0:
            self.process_collection.await_termination_of_any_process()

        xml_parser = XmlResultParser()
        instances_results = []
        for id in range(self.num_processes):
            try:
                xml_results = xml_parser.parse(xml_files[id])
            except Exception as e:
                xml_results = str(e)

            instance_results = {"id": id,
                                "cmd": cmds[id],
                                "diversification": dynamic_args_selection[id],
                                "xml": xml_results}
            instances_results.append(instance_results)

        return instances_results
