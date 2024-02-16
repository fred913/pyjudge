import json
import os
import tomllib
import toml
import tomli_w


def convert_toml_to_json_md(toml_dir, output_dir):
    toml_files = os.listdir(toml_dir)

    for toml_file in toml_files:
        problem_id = os.path.splitext(toml_file)[0]

        with open(os.path.join(toml_dir, toml_file), "rb") as f:
            metadata = tomllib.load(f)

        descriptions = metadata.pop("descriptions")

        with open(os.path.join(output_dir, problem_id, "info.json"),
                  "w",
                  encoding="utf-8") as f:
            json.dump(metadata, f, ensure_ascii=False, indent=2)

        with open(os.path.join(output_dir, problem_id, "description.md"),
                  "w",
                  encoding="utf-8") as f:
            f.write(descriptions)


# Example usage
toml_dir = "./problems.toml"
output_dir = "./problems"

convert_toml_to_json_md(toml_dir, output_dir)
