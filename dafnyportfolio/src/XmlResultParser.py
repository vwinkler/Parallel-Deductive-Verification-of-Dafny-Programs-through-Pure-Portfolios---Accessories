import xml.etree.ElementTree as et
from datetime import datetime


class MissingElementException(RuntimeError):
    def __init__(self, missing_tag, parent):
        self.parent = parent
        self.missing_tag = missing_tag
        if isinstance(parent, et.ElementTree):
            message = "Root element is not '{}' (it is '{}')".format(self.missing_tag, self.parent.getroot().tag)
        else:
            message = "Missing element with tag '{}' in element with tag '{}'".format(self.missing_tag, self.parent.tag)
        super().__init__(message)


class MissingAttributeException(RuntimeError):
    def __init__(self, missing_attribute_name, parent):
        self.parent = parent
        self.missing_attribute_name = missing_attribute_name

        message = "Missing attribute with name '{}' in element with tag '{}'".format(self.missing_attribute_name,
                                                                                     self.parent)
        super().__init__(message)


class XmlResultParser:
    def parse(self, file):
        tree = et.parse(file)
        return self._parse_boogie_element(tree.getroot())

    def _try_find_element(self, parent, tag):
        element = parent.find(tag)
        if element is None:
            raise MissingElementException(tag, parent)
        return element

    def _parse_boogie_element(self, boogie_element):
        return {"version": self._parse_version_attribute_value(self._try_get_attribute(boogie_element, "version")),
                "command": self._parse_command_line_attribute_value(
                    self._try_get_attribute(boogie_element, "commandLine")),
                "methods": self._parse_methods(boogie_element.iterfind("method"))}

    def _parse_version_attribute_value(self, version_attribute_value):
        return version_attribute_value

    def _parse_command_line_attribute_value(self, command_line_attribute_value):
        return command_line_attribute_value

    def _parse_methods(self, methods_elements):
        methods = []
        for methodElement in methods_elements:
            methods.append(self._parse_method(methodElement))
        return methods

    def _parse_method(self, method_element):
        result = {"name": self._parse_method_name_attribute_value(self._try_get_attribute(method_element, "name")),
                  "startTime": self._parse_time_attribute_value(self._try_get_attribute(method_element, "startTime"))}

        try:
            conclusion_element = self._try_find_element(method_element, "conclusion")
        except MissingElementException:
            return self.make_unconcluded_method_result(result)

        conclusion = self._parse_conclusion(conclusion_element)
        result["finished"] = True
        result["endTime"] = conclusion["endTime"]
        result["duration"] = conclusion["duration"]
        result["outcome"] = conclusion["outcome"]
        return result

    def make_unconcluded_method_result(self, method_result_before_conclusion):
        result = method_result_before_conclusion.copy()
        result["finished"] = False
        result["endTime"] = None
        result["outcome"] = None
        return result

    def _try_get_attribute(self, element, name):
        value = element.get(name)
        if value is None:
            raise MissingAttributeException(element, name)
        return value

    def _parse_method_name_attribute_value(self, method_name_attribute_value):
        return method_name_attribute_value

    def _parse_time_attribute_value(self, time_attribute_value):
        return datetime.strptime(time_attribute_value, "%Y-%m-%d %H:%M:%S%z")

    def _parse_conclusion(self, conclusion_element):
        return {"endTime": self._parse_time_attribute_value(self._try_get_attribute(conclusion_element, "endTime")),
                "outcome": self._parse_outcome_attribute_value(self._try_get_attribute(conclusion_element, "outcome")),
                "duration": self._parse_duration_attribute_value(
                    self._try_get_attribute(conclusion_element, "duration"))}

    def _parse_outcome_attribute_value(self, outcome_attribute_value):
        return outcome_attribute_value

    def _parse_duration_attribute_value(self, duration_attribute_value):
        return float(duration_attribute_value)
