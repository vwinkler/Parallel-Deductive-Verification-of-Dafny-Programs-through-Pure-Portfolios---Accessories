import json
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
        for id in range(self.num_processes):
            static_args = [self.dafny_command, self.filename, proc_argument, self._make_xml_arg(id)]
            dynamic_args = dynamic_args_selection[id]
            self.process_collection.start_process(static_args + dynamic_args)

        while self.process_collection.count_running_processes() > 0:
            self.process_collection.await_termination_of_any_process()

        xml_parser = XmlResultParser()
        instances_results = []
        for id in range(self.num_processes):
            try:
                xml_results = xml_parser.parse(self._make_xml_filename(id))
            except Exception as e:
                xml_results = str(e)

            instance_results = {"id": id,
                                "diversification": dynamic_args_selection[id],
                                "xml": xml_results}
            instances_results.append(instance_results)

        return instances_results

    def _make_xml_arg(self, id):
        return "/xml:{}".format(self._make_xml_filename(id))

    def _make_xml_filename(self, id):
        filename = os.path.splitext(os.path.basename(self.filename))[0]
        return "{}_{}.xml".format(filename, id)
