import tkinter
from tkinter import Canvas
from datetime import date, datetime


class MainApp(tkinter.Frame):
    def __init__(self, parent, *args, **kwargs):
        tkinter.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent

        # Create a canvas called c 800x800px
        c = Canvas(root, width=800, height=800, bg='light blue')
        # Pack the canvas into the window
        c.pack()
        # Add text into the canvas, starts at x=100, y=50
        # The anchor parameter controls the positioning of an item in terms of its coordinates.
        c.create_text(400, 10, anchor='n', fill='black', font='Courier 28 italic bold', text='My Countdown Calendar')
        events = self.get_events()
        today = date.today()
        vertical_space = 100
        events.sort(key=lambda x: x[1])
        for event in events:
            event_name = event[0]
            event_date = event[1]
            days_until = self.days_between_dates(event_date, today)
            display = '-> It is {} days until {}'.format(days_until, event_name)
            if int(days_until) <= 7:
                text_col = 'red'
            else:
                text_col = 'black'
            if int(days_until) <= 0:
                display = '-> {} has expired'.format(event_name)
            c.create_text(10, vertical_space, anchor='w', fill=text_col, font='Courier 15 bold italic', text=display)
            vertical_space += 25

    def str_to_date(self, v):
        return datetime.strptime(str(v), '%d/%m/%Y').date()

    def get_events(self):
        list_events = []
        with open('events.txt') as file:
            for line in file:
                if line != '\n':
                    line = line.rstrip('\n')
                    current_event = line.split(',')
                    event_date = self.str_to_date(current_event[1])
                    current_event[1] = event_date
                    list_events.append(current_event)
        return list_events

    def days_between_dates(self, date1, date2):
        time_between = str(date1 - date2)
        number_of_days = time_between.split(' ')
        return number_of_days[0]


if __name__ == '__main__':
    root = tkinter.Tk()
    MainApp(root).pack(side='top', fill='both', expand=True)
    root.mainloop()
