def validate_name(name):
    if not name or not isinstance(name, str):
        return False
    return all(c.isalpha() or c.isspace() for c in name) and len(name.strip()) >= 2