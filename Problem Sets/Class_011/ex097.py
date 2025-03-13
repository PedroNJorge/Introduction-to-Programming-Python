def division(a, b):
    try:
        return f"{a}/{b} = {a/b}"
    except ZeroDivisionError:
        return "Error: Division by 0!"
    except TypeError:
        return "Error: Unsupported type(s) for division!"
