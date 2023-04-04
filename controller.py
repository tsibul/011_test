from menu import print_menu


def process_flow(note_list, menu_item, menu_key):
    print_menu(menu_item, menu_key)
    print()
    input_key =input('Input menu item: ')
    if input_key in menu_item.keys():
        if menu_key == 'Main Menu' or input_key == '0':
            menu_item, menu_key = menu_item[input_key][1](note_list)
        else:
            menu_item[input_key][1](note_list)
    else:
        print('!!! Wrong input !!!!')
        return menu_item, menu_key
    return menu_item, menu_key