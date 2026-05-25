def normalize_name(name):

    return name.lower().replace(" ", "_")


def generate_api_schema(intent_data):

    modules = intent_data["modules"]

    endpoints = []

    for module in modules:

        normalized = normalize_name(module)

        endpoint = {
            "path": f"/api/{normalized}",
            "method": "GET",
            "description": f"Fetch {normalized} data"
        }

        endpoints.append(endpoint)

    return {
        "api_schema": endpoints
    }