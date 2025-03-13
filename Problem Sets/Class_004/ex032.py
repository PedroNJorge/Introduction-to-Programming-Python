def approximate_sqrt(x, max_error):
    y0 = x / 2
    yn = 0.5*(y0 + x/y0)

    while abs(yn - y0) >= max_error:
        y0 = yn
        yn = 0.5*(y0 + x/y0)
    
    return yn
