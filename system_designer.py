def generate_system_design(intent_data):

    app_name = intent_data["app_name"]

    modules = intent_data["modules"]

    roles = intent_data["roles"]

    design = {
        "app_name": app_name,

        "frontend": {
            "pages": modules
        },

        "backend": {
            "services": modules
        },

        "database": {
            "tables": modules
        },

        "auth": {
            "roles": roles
        }
    }

    return design