def variableName(name):
    return name.replace("_", "").isalnum() and not name[0].isdigit()
