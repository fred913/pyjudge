import json
import os

import toml
import tomli_w

l = os.listdir("./problems/")

for problem_id in l:
    with open(f"problems/{problem_id}/info.json", "r", encoding="utf-8") as f:
        metadata = json.load(f)
    with open(f"problems/{problem_id}/description.md", "r",
              encoding="utf-8") as f:
        metadata['descriptions'] = f.read()

    with open(f"problems.toml/{problem_id}.toml", "wb") as f:
        tomli_w.dump(metadata, f, multiline_strings=True)
