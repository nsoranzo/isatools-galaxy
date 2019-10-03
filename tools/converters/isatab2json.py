#!/usr/bin/env python3

import json
import sys

input_path = sys.argv[1]
output_file_path = sys.argv[2]

try:
    from isatools.convert import isatab2json
except ImportError:
    raise RuntimeError('Could not import isatools package')

isatab_dir = input_path
print("THIS IS OUR INPUT:", isatab_dir)
my_json = isatab2json.convert(
    work_dir=isatab_dir, validate_first=False, use_new_parser=True)
with open(output_file_path, 'w') as out_fp:
    json.dump(my_json, out_fp, indent=4)
    print("is it?", json.dump(my_json, out_fp, indent=4))
print("THIS IS THE OUTPUT GENERATED BY GALAXY:", out_fp.name)