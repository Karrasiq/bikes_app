def to_json(python_type):
    from json import dumps

    json_string = dumps(python_type)

    return json_string
