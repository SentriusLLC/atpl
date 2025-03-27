
# Python test to validate that the invalid example fails
# File: tests/test_invalid_policy.py

import json
import yaml
import jsonschema
from pathlib import Path

schema_file = Path(__file__).parent.parent / 'atpl.schema.json'
invalid_example = Path(__file__).parent.parent / 'examples' / 'invalid-missing-fields.yaml'

with open(schema_file) as sf:
    schema = json.load(sf)


try:
    with open(invalid_example) as ef:
        example = yaml.safe_load(ef)

    jsonschema.validate(instance=example, schema=schema)
    print("❌ Test failed: Invalid policy was incorrectly accepted")
except jsonschema.ValidationError as e:
    print("✅ Correctly failed validation:", e.message)
