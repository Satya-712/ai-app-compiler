import json

REQUIRED_FIELDS = [
    "app_name",
    "modules",
    "roles",
    "features"
]

def validate_output(data):

    errors = []

    for field in REQUIRED_FIELDS:
        if field not in data:
            errors.append(f"Missing field: {field}")

    if not isinstance(data.get("modules", []), list):
        errors.append("modules must be a list")

    if not isinstance(data.get("roles", []), list):
        errors.append("roles must be a list")

    if not isinstance(data.get("features", []), list):
        errors.append("features must be a list")

    return errors