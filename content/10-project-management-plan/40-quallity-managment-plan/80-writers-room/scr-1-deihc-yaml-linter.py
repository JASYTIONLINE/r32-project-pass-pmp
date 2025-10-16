#!/usr/bin/env python3

import os
import yaml
import re

REQUIRED_FIELDS = [
    "title", "date", "draft", "tags",
    "function", "shortcode", "classification",
    "retention", "integrityCheck"
]

def validate_yaml(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()

        if not (lines[0].strip() == "---"):
            return file_path, "Missing opening --- for YAML"

        try:
            end_index = lines[1:].index("---\n") + 1
        except ValueError:
            return file_path, "Missing closing --- for YAML"

        yaml_block = "".join(lines[1:end_index])
        metadata = yaml.safe_load(yaml_block)

        if not isinstance(metadata, dict):
            return file_path, "YAML block is not a dictionary"

        missing = [field for field in REQUIRED_FIELDS if field not in metadata]
        if missing:
            return file_path, f"Missing fields: {', '.join(missing)}"

        return file_path, "OK"
    except Exception as e:
        return file_path, f"Error: {str(e)}"

def main():
    repo_root = "."  # Change to your vault root if needed
    for root, dirs, files in os.walk(repo_root):
        for file in files:
            if file.endswith(".md"):
                path = os.path.join(root, file)
                result = validate_yaml(path)
                if result[1] != "OK":
                    print(f"[!] {result[0]} → {result[1]}")

if __name__ == "__main__":
    main()
