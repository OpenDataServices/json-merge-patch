import unittest
import merge

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


if __name__ == '__main__':
    unittest.main()




