from start_end import start_notes
from outputs import all_notes
from menu import menu, print_menu, view_note_by_date, view_note_by_id
from controller import process_flow

notes_list = start_notes()

menu_key = 'Main Menu'
menu_item = menu[menu_key]

while not isinstance(menu_item, tuple) or menu_item[0] != 'Exit':
    menu_item, menu_key = process_flow(notes_list, menu_item, menu_key)
# all_notes(notes_list)

#note = view_note_by_id(notes_list)
#note2 = view_note_by_date(notes_list)
print()
#exit_notes(notes_list)
