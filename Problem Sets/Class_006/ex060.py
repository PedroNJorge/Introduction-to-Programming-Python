def eeny_meeny(lst, k):
    n = len(lst)
    rm = []
    n_init = 0
    for i in range(n):
        mod = k % (n-i)
        rm_mod_index = (mod + n_init - 1) % (n-i)

        rm.append(lst[rm_mod_index])
        del lst[rm_mod_index]

        n_init = (rm_mod_index + 1) % (n-i)
        if rm_mod_index < n_init:
            n_init = (n_init - 1) % (n-i)
    return rm


'''
print(eeny_meeny(["Milhouse","Bart","Jessica","Nikki","Terri"], 10))
print(eeny_meeny(["PedroR","Miriam","Alberto","Tadeu","Francesco","PedroM"], 3))
'''
