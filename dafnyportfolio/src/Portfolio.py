from ProcessCollection import *


class Portfolio:
    def __init__(self, filename, procedure_name, num_processes, option_selector):
        self.option_selector = option_selector
        self.num_processes = num_processes
        self.filename = filename
        self.procedure_name = procedure_name
        self.process_collection = ProcessCollection()

    def run(self):
        proc_argument = "/proc:*{}".format(self.procedure_name)

        dynamic_args_selection = self.option_selector.create_arguments(self.num_processes)
        for id in range(self.num_processes):
            static_args = ["dafny", self.filename, proc_argument, self._make_xml_arg(id)]
            dynamic_args = dynamic_args_selection[id]
            self.process_collection.start_process(static_args + dynamic_args)

        while self.process_collection.count_running_processes() > 0:
            self.process_collection.await_termination_of_any_process()

    def _make_xml_arg(self, id):
        return "/xml:{}_{}.xml".format(self.filename, id)
