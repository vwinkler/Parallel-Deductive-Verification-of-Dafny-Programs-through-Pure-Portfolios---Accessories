import unittest

from dafnyportfolio.src.job_creation.expand import expand, resolve_includes, resolve_cartconcat


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

    def test_dict_with_noexpand_list(self):
        example = {"[noexpand]x": [1, 2, 3], "y": 0}
        expectation = [{"x": [1, 2, 3], "y": 0}]
        self.assertCountEqual(expectation, expand(example))

    def test_noexpand_on_dict(self):
        example = {"[noexpand]x": {"y": 0}}
        expectation = [{"x": [{"y": 0}]}]
        self.assertCountEqual(expectation, expand(example))

    def test_noexpand_on_dict_with_list(self):
        example = {"[noexpand]x": {"y": [0, 1]}}
        expectation = [{"x": [{"y": 0}, {"y": 1}]}]
        self.assertCountEqual(expectation, expand(example))

    def test_dict_with_multiple_lists(self):
        example = {"x": [1, 2, 3], "y": [4, 5]}
        expectation = [{"x": 1, "y": 4}, {"x": 2, "y": 4}, {"x": 3, "y": 4}, {"x": 1, "y": 5}, {"x": 2, "y": 5},
                       {"x": 3, "y": 5}]
        self.assertCountEqual(expectation, expand(example))

    def test_dict_with_list_and_noexpand_list(self):
        example = {"x": [1, 2, 3], "[noexpand]y": [4, 5]}
        expectation = [{"x": 1, "y": [4, 5]}, {"x": 2, "y": [4, 5]}, {"x": 3, "y": [4, 5]}]
        self.assertCountEqual(expectation, expand(example))

    def test_dict_with_noexpand_list_with_dict_with_list(self):
        example = {"[noexpand]x": [{"x": [1, 2, 3]}, {"x": [4, 5, 6]}]}
        expectation = [{"x": [{"x": 1}, {"x": 2}, {"x": 3}, {"x": 4}, {"x": 5}, {"x": 6}]}]
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

    def test_cartconcat(self):
        example = [{"[cartconcat]x": [[0], [1, 2, 3]]}]
        expectation = [{"x": [0, 1]}, {"x": [0, 2]}, {"x": [0, 3]}]
        self.assertCountEqual(expectation, expand(example))

    def test_cartconcat_empty(self):
        example = [{"[cartconcat]x": [[[]], [1, 2, 3]]}]
        expectation = [{"x": [1]}, {"x": [2]}, {"x": [3]}]
        self.assertCountEqual(expectation, expand(example))

    def test_cartconcat_single(self):
        example = [{"[cartconcat]x": [0, [1, 2, 3]]}]
        expectation = [{"x": [0, 1]}, {"x": [0, 2]}, {"x": [0, 3]}]
        self.assertCountEqual(expectation, expand(example))

    def test_cartconcat_multiple(self):
        example = [{"[cartconcat]x": [[[0, 1]], [[2], [3]]]}]
        expectation = [{"x": [0, 1, 2]}, {"x": [0, 1, 3]}]
        self.assertCountEqual(expectation, expand(example))

    def test_cartconcat_practice(self):
        example = {"[cartconcat]stdin": [
            [
                [],
                ["/proverOpt:O:smt.qi.eager_threshold=30"]
            ],
            [
                "",
                "/vcsMaxKeepGoingSplits:2 /vcsKeepGoingTimeout:1"
            ]
        ]}

        expectation = [
            {"stdin": [""]},
            {"stdin": ["/vcsMaxKeepGoingSplits:2 /vcsKeepGoingTimeout:1"]},
            {"stdin": ["/proverOpt:O:smt.qi.eager_threshold=30", ""]},
            {"stdin": ["/proverOpt:O:smt.qi.eager_threshold=30", "/vcsMaxKeepGoingSplits:2 /vcsKeepGoingTimeout:1"]}
        ]
        self.assertCountEqual(expectation, expand(example))


def test_nested_cartconcat(self):
    example = [
        {
            "[cartconcat]x": [
                {
                    "[cartconcat]x": [
                        [0],
                        [1, 2, 3]
                    ]
                },
                [4, 5, 6]
            ]
        }
    ]
    expectation = [
        {
            "x": [
                [{"x": [[0, 1], [0, 2], [0, 3]]}, 4],
                [{"x": [[0, 1], [0, 2], [0, 3]]}, 5],
                [{"x": [[0, 1], [0, 2], [0, 3]]}, 6]
            ]
        }
    ]
    self.assertCountEqual(expectation, resolve_cartconcat(example))


if __name__ == '__main__':
    unittest.main()
