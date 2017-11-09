import unittest
import lib as merge
from collections import OrderedDict

fixtures = [
[{
    "title": "Goodbye!",
    "author" : {
        "givenName" : "John",
        "familyName" : "Doe"
    },
    "tags":[ "example", "sample" ],
    "content": "This will be unchanged"
},
{
    "title": "Hello!",
    "phoneNumber": "+01-123-456-7890",
    "author": {
        "familyName": None
     },
     "tags": [ "example" ]
},
{
     "title": "Hello!",
     "author" : {
         "givenName" : "John"
     },
     "tags": [ "example" ],
     "content": "This will be unchanged",
     "phoneNumber": "+01-123-456-7890"
}],
[{"a":"b"},{"a":"c"},{"a":"c"}],
[{"a":"b"},{"b":"c"},{"a":"b", "b":"c"}],
[{"a":"b"},{"a":None},{}],
[{"a":"b","b":"c"},{"a":None},{"b":"c"}],
[{"a":["b"]},{"a":"c"},{"a":"c"}],
[{"a":"c"},{"a":["b"]},{"a":["b"]}],
[{"a": {"b": "c"}},{"a":{"b": "d", "c": None}}, {"a": {"b": "d"}}],
[{"a": [{"b":"c"}]},{"a": [1]},{"a": [1]}],
[["a","b"],["c","d"],["c","d"]],
[{"a":"foo"},None,None],
[{"a":"foo"},"bar","bar"],
[{"e":None},{"a":1},{"e":None, "a":1}],
[[1,2], {"a":"b","c":None},{"a":"b"}],
[{},{"a":{"bb":{"ccc": None}}},{"a":{"bb":{}}}]
]


class TestAll(unittest.TestCase):

    def test_merge(self):
        for fixture in fixtures:
            self.assertEqual(merge.merge(fixture[0], fixture[1]), fixture[2])

    def test_create_patch(self):
        for num, fixture in enumerate(fixtures):
            # ignore some tests as these do not show mimimum patch needed
            if num not in [7, 13, 14]:
                self.assertEqual(merge.create_patch(fixture[0], fixture[2]), fixture[1])


ordered_fixtures = [[
    OrderedDict([
        ("title", "Goodbye!"),
        ("content", "This will be unchanged")
    ]),
    OrderedDict([
        ("title", "Goodbye!"),
        ("new", "Where will this go?"),
        ("content", "content")
    ]),
    OrderedDict([
        ("title", "Goodbye!"),
        ("content", "content"),
        ("new", "Where will this go?")
    ]),
    OrderedDict([
        ("new", "Where will this go?"),
        ("title", "Goodbye!"),
        ("content", "content")
    ])
],[
    OrderedDict([
        ("title", "Goodbye!"),
        ("content", "This will be unchanged")
    ]),
    OrderedDict([
        ("title", "Goodbye!"),
        ("new", OrderedDict([("where", "will I go")])),
        ("content", "content"),
    ]),
    OrderedDict([
        ("title", "Goodbye!"),
        ("content", "content"),
        ("new", OrderedDict([("where", "will I go")])),
    ]),
    OrderedDict([
        ("new", OrderedDict([("where", "will I go")])),
        ("title", "Goodbye!"),
        ("content", "content"),
    ])
]]

class TestOrdered(unittest.TestCase):

    def test_merge(self):
        for fixture in ordered_fixtures:
            self.assertEqual(merge.merge(fixture[0].copy(), fixture[1], position='last'), fixture[2])
            self.assertEqual(merge.merge(fixture[0].copy(), fixture[1], position='first'), fixture[3])

if __name__ == '__main__':
    unittest.main()




