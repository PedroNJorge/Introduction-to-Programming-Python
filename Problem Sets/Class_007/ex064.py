def rename(menu, old_name, new_name):
    if old_name in menu.keys():
        menu[new_name] = menu[old_name]
        del menu[old_name]
