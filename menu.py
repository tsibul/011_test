from outputs import all_notes, note_by_date, note_by_id
from edits import add_note, update_note, delete_note
from start_end import finish_notes


def view_note_by_date(notes_list):
    date = input('Enter the date in format dd.mm.YYYY : ')
    notes = note_by_date(date, notes_list)
    if notes:
        for note in notes:
            print(note)
    else:
        print("!!! Date doesn't exists !!!")


def view_note_by_id(notes_list):
    note_id = input('Enter the note id : ')
    note = note_by_id(note_id, notes_list)
    if note:
        print(note)
    else:
        print('!!! Wrong id !!!')


def exit_notes(notes_list):
    finish_notes(notes_list)
    return ('Exit', None), None


def to_main_nenu(notes_list):
    menu_key = 'Main Menu'
    menu_item = menu[menu_key]
    return menu_item, menu_key


def to_view_menu(notes_list):
    menu_key = 'View Menu'
    menu_item = menu[menu_key]
    return menu_item, menu_key


def to_edit_menu(notes_list):
    menu_key = 'Edit Menu'
    menu_item = menu[menu_key]
    return menu_item, menu_key



main_menu = {
    '1': ('View notes', to_view_menu),
    '2': ('Edit notes', to_edit_menu),
    '0': ('Exit', exit_notes)
}

view_menu = {
    '1': ('View all', all_notes),
    '2': ('Filter by date', view_note_by_date),
    '3': ('Find by id', view_note_by_id),
    '0': ('Return to Main menu', to_main_nenu)
}

edit_menu = {
    '1': ('Add record', add_note),
    '2': ('Edit record', update_note),
    '3': ('Delete record', delete_note),
    '0': ('Return to Main menu', to_main_nenu)
}

menu = {
    'Main Menu': main_menu,
    'View Menu': view_menu,
    'Edit Menu': edit_menu
}


def print_menu(item, item_key):
    print()
    print('= ' + item_key + ' =')
    for key in item.keys():
        print(key + ' ' + item[key][0])

