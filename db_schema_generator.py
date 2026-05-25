def normalize_name(name):

    return name.lower().replace(" ", "_")


def generate_db_schema(intent_data):

    modules = intent_data["modules"]

    tables = []

    for module in modules:

        normalized = normalize_name(module)

        table = {
            "table_name": normalized,
            "fields": [
                {
                    "name": "id",
                    "type": "integer"
                },
                {
                    "name": "created_at",
                    "type": "datetime"
                }
            ]
        }

        tables.append(table)

    return {
        "database_schema": tables
    }