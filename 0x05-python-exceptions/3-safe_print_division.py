#!/usr/bin/python3
def safe_print_division(a, b):
    c = 0
    try:
        c = a / b
        return c
    except Exception:
        return None
    finally:
        print("Inside result: {}".format(c if c > 0 else None))
