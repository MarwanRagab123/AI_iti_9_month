def validate_password(password):
    if not password or not isinstance(password, str):
        return False
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(c in '!@#$%^&*()-_=+[]{}|;:,.<>?/' for c in password)
    is_long_enough = len(password) >= 8
    return all([has_upper, has_lower, has_digit, has_special, is_long_enough])
def confirm_password(password, confirm):
    if not password or not confirm:
        return False
    return password == confirm