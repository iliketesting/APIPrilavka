import data


def modify_create_kit_body(name):
    return modify_kit_body ("name", name)


def modify_kit_body (key, value):
    body = data.KIT_BODY.copy()
    body[key] = value

    return body