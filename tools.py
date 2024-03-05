import json
import random
import datetime

def jsonlines_load_file(fname: str):
    lines = []
    with open(fname, 'r') as f:
        for line in f:
            lines.append(json.loads(line))
    return lines

def jsonlines_load(fname: str, start: int, end: int):
    lines = []
    with open(fname, 'r') as f:
        for line in f:
            lines.append(json.loads(line))
    random_lines = lines[start:end]
    return random_lines

def append_json_to_file(ouputfolder: str, fname_prefix: str, data: dict):
    file_name = f'{fname_prefix}.jsonl'
    file_name_with_folder = f'{ouputfolder}/{file_name}'
    with open(file_name_with_folder, 'a') as f:
        json.dump(data, f)
        f.write("\n")