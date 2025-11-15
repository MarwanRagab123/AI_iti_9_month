def validate_mobile_egy(mobile):
    if not mobile or not isinstance(mobile, str):
        return False
    if len(mobile) != 11 or not mobile.isdigit():
        return False
    if not mobile.startswith('01'):
        return False
    if mobile[2] not in '0125':
        return False
    return True