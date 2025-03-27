# Python test to validate a correct example
# File: tests/test_validation.py

import json
import yaml
import jsonschema
from pathlib import Path

schema_file = Path(__file__).parent.parent / 'atpl.schema.json'
example_file = Path(__file__).parent.parent / 'examples' / 'trust-observer.yaml'

with open(schema_file) as sf:
    schema = json.load(sf)

with open(example_file) as ef:
    example = yaml.safe_load(ef)

try:
    jsonschema.validate(instance=example, schema=schema)
    print("✅ Policy is valid!")
except jsonschema.ValidationError as e:
    print("❌ Validation failed:", e.message)