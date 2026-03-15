def try_parse_int(value):
    try:
        return True, int(value)
    except ValueError:
        return False, None