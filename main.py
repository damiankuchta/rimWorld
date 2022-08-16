from random import random
import PySimpleGUI as sg
from resources import resources

from Colony import Colony


def display_data(colony):
    print(colony)


def feed_colonist(colony):
    colony.feed_colonist()


def take_action(colony):
    colony.take_actions(colony)


def pick_event(colony):
    pass


def execute_event(colony):
    pass


def next_round(colony):
    feed_colonist(colony)
    display_data(colony)
    take_action(colony)



def main():
    colony = Colony()

    sg.theme('DarkAmber')  # Add a touch of color
    # All the stuff inside your window.
    layout = [[sg.Text('Some text on Row 1')],
              [sg.Text('Enter something on Row 2'), sg.InputText()],
              [sg.Button('Next round'), sg.Button('Cancel')],
              [sg.Table(values=[[r, colony.resources[r]] for r in resources],
                        hide_vertical_scroll=True,
                        headings=['Resources', 'Amount'])]]

    # Create the Window
    window = sg.Window('Window Title', layout)
    # Event Loop to process "events" and get the "values" of the inputs
    while True:  # Event Loop
        event, values = window.read()
        print(event, values)
        if event == sg.WIN_CLOSED or event == 'Exit':
            break
        if event == 'Next round':
            # window.Element('-LISTBOX-').update(values=['new value 1', 'new value 2', 'new value 3'])
            window['-OUTPUT-'].update(values['-IN-'])

    window.close()


if __name__ == '__main__':
    main()
