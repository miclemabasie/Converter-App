import PySimpleGUI as sg
import logging

logger = logging.getLogger(__name__)


def main():
    ''''
        The number of nested list represents the number of rows the app is going to have in the main layout.
        And this is going to determine the hieght of the window
    '''
    layout = [
        [sg.Text("Text", enable_events=True, key="-TEXT-"),
         sg.Spin(['item1', 'item2'])],
        [sg.Button("Button", key="-BUTTON1-")],
        [sg.Input()],
        [sg.Text("Hello"), sg.Button("Test button", key="-BUTTON2-")]
    ]

    window = sg.Window("Converter", layout)
    while True:
        event, value = window.read()  # Returns an event and values.

        if event == sg.WIN_CLOSED:
            break

        if event == "-BUTTON-":
            print('This fuckent test button is pressed.')

        if event == '-TEXT-':
            print('The text was pressed')

    window.close()


if __name__ == '__main__':
    main()
