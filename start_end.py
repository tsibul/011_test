from models import Notes
import os


def start_notes():
    '''
        :return: list of notes imported from csv
    '''
    notes_list = []
    with open('notes.csv', 'r') as db_file:
        for line in db_file:
            notes_list.append(Notes(line[:-1].split(';')))
    return notes_list


def finish_notes(notes_list):
    '''
        :param notes_list: export to notes.csv
    '''
    os.remove('notes.csv')
    with open('notes.csv', 'w') as db_file:
        for note in notes_list:
            db_file.write(note.to_csv())
