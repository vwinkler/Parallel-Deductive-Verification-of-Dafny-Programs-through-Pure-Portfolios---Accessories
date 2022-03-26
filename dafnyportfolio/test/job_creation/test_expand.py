import unittest

from dafnyportfolio.src.job_creation.expand import expand, resolve_includes


class ExpandTest(unittest.TestCase):
    def test_no_list(self):
        example = {"x": 0, "y": 1}
        expectation = [example]
        self.assertCountEqual(expectation, expand(example))

    def test_nested_no_list(self):
        example = {"x": {"a": 2, "b": 3}, "y": {"a": 2, "b": 3}}
        expectation = [example]
        self.assertCountEqual(expectation, expand(example))

    def test_only_list(self):
        example = [1, 2, 3]
        expectation = example
        self.assertCountEqual(expectation, expand(example))

    def test_dict_with_list(self):
        example = {"x": [1, 2, 3], "y": 0}
        expectation = [{"x": 1, "y": 0}, {"x": 2, "y": 0}, {"x": 3, "y": 0}]
        self.assertCountEqual(expectation, expand(example))

    def test_dict_with_multiple_lists(self):
        example = {"x": [1, 2, 3], "y": [4, 5]}
        expectation = [{"x": 1, "y": 4}, {"x": 2, "y": 4}, {"x": 3, "y": 4}, {"x": 1, "y": 5}, {"x": 2, "y": 5},
                       {"x": 3, "y": 5}]
        self.assertCountEqual(expectation, expand(example))

    def test_list_with_list(self):
        example = [1, [2, 3]]
        expectation = [1, 2, 3]
        self.assertCountEqual(expectation, expand(example))

    def test_list_with_list_with_list(self):
        example = [1, [2, [3, 4]]]
        expectation = [1, 2, 3, 4]
        self.assertCountEqual(expectation, expand(example))

    def test_list_of_multiple_lists(self):
        example = [[1, 2], [3, 4]]
        expectation = [1, 2, 3, 4]
        self.assertCountEqual(expectation, expand(example))

    def test_list_with_dict_with_list(self):
        example = [{"x": [1, 2]}, 0]
        expectation = [{"x": 1}, {"x": 2}, 0]
        self.assertCountEqual(expectation, expand(example))

    def test_include(self):
        example = [{"[include]x": {"y": 1}, "y": 0}]
        expectation = [{"y": 1}]
        self.assertCountEqual(expectation, resolve_includes(example))

    def test_include_no_overwrite(self):
        example = {"[include]x": {"y": 1}}
        expectation = {"y": 1}
        self.assertCountEqual(expectation, resolve_includes(example))

    def test_nested_include(self):
        example = [{"[include]": {"[include]": {"y": 0}}}]
        expectation = [{"y": 0}]
        self.assertCountEqual(expectation, resolve_includes(example))

    if __name__ == '__main__':
        unittest.main()
