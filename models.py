import datetime


class Notes:

    def __init__(self, *args):
        '''
        :param args:
        0 — note id
        1 — note title
        2 — note text
        '''
        self.note_id = args[0]
        self.title = args[1]
        self.text = args[2]
        self.date = datetime.date.today()
        self.time = datetime.datetime.now().time()

    def __repr__(self):
        return str(self.note_id) + ' ' + datetime.datetime.strftime(self.date,
                                                                    '%d.%m.%Y') + ' ' + self.title + ' ' + self.text

    def __str__(self):
        return str(self.note_id) + ' ' + datetime.datetime.strftime(self.date,
                                                                    '%d.%m.%Y') + ' ' + self.title + ' ' + self.text
