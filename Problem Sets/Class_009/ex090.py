def rec(lst, cur, digits, k, n, d):
    if len(cur) == k:
        lst.append(cur)
    else:
        esp_rest = k - len(cur)
        num_d_para_add = n - cur.count(str(d))
        r = range(10)

        if esp_rest > num_d_para_add:
            if num_d_para_add == 0:
                r = digits
            for i in r:
                rec(lst, cur + str(i), digits, k, n, d)

        elif esp_rest == num_d_para_add:
            lst.append(cur + str(d)*num_d_para_add)


def numbers(k, n, d):
    '''
    k -> len da str
    n -> nº de vezes que d aparece
    d -> digito
    '''
    digits = [i for i in range(10) if i != d]
    lst = []
    rec(lst, "", digits, k, n, d)
    result = [int(x) for x in lst if x[0] != "0"]
    return result
