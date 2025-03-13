def future_exceptions(f, a, b):
    error_counter = 0
    for i in range(a, b+1):
        try:
            f(i)
        except:
            error_counter += 1
    return error_counter
