def repair_output(data):

    if "features" not in data:
        data["features"] = []

    if "roles" not in data:
        data["roles"] = ["user"]

    return data