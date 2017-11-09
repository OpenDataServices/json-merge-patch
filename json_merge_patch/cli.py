from __future__ import print_function
import argparse
import json_merge_patch
import json
from collections import OrderedDict


def merge(files, output, position):
    result = None
    for file in files:
        with open(file) as input_file:
            input_json = json.load(input_file, object_pairs_hook=OrderedDict)
        if result is None:
            result = input_json
        else:
            result = json_merge_patch.merge(result, input_json, position=position)

    merged = json.dumps(result, indent=4)

    if output:
        with open(output, 'w+') as output_file:
            output_file.write(merged)
    else:
        print(merged)

def create_patch(original, target, output):
    with open(original) as original_file, open(target) as target_file:
        original_json = json.load(original_file)
        target_json = json.load(target_file)
        result = json_merge_patch.create_patch(original_json, target_json)

    patch = json.dumps(result, indent=4)

    if output:
        with open(output, 'w+') as output_file:
            output_file.write(patch)
    else:
        print(patch)



def main():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest='subparser_name')
    parser_merge = subparsers.add_parser(
      'merge', help='Merge json documents together using JSON merge patch')

    parser_merge.add_argument('-o', '--output', help='path of output file, if none specified will print to stdout')
    parser_merge.add_argument('-f', '--first', action='store_true', help='when merging new properties of object put them first instead of last')
    parser_merge.add_argument('files', help='JSON files to merge in order', nargs='+')

    parser_create_patch = subparsers.add_parser(
      'create-patch', help='Make a patch file comparing two json files.')

    parser_create_patch.add_argument('-o', '--output', help='path of output file, if none specified will print to stdout')
    parser_create_patch.add_argument('original', help='JSON file you want to patch')
    parser_create_patch.add_argument('target', help='JSON files to merge in order')

    args = parser.parse_args()   
    if args.subparser_name == 'merge':
        merge(args.files, args.output, 'first' if args.first else 'last')
    elif args.subparser_name == 'create-patch':
        create_patch(args.original, args.target, args.output)
    else:
        parser.print_help()
