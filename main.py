import PySimpleGUI as sg
import logging

logger = logging.getLogger(__name__)


def main():
    ''''
        The number of nested list represents the number of rows the app is going to have in the main layout.
        And this is going to determine the hieght of the window
    '''
    layout = [
        # [sg.Text("Text", enable_events=True, key="-TEXT-"),
        #  sg.Spin(['item1', 'item2'])],
        # [sg.Button("Button", key="-BUTTON1-")],
        # [sg.Input(key='-INPUT-')],
        # [sg.Text("Hello"), sg.Button("Test button", key="-BUTTON2-")]

        [sg.Input(key='-INPUT-'), sg.Spin(['km to mile', 'kg to pound',
                                           'mile to km', 'sec to min'], key="-CONVERT TO-"), sg.Button("Convert", key='-CONVERT-')],
        [sg.Text(key="-OUTPUT-")]

    ]

    window = sg.Window("Converter", layout)
    while True:
        event, values = window.read()  # Returns an event and values.

        if event == sg.WIN_CLOSED:
            break

        if event == '-CONVERT-':
            input_value = values['-INPUT-']
            if input_value.isnumeric():
                input_value = int(input_value)
                unit = values['-CONVERT TO-']
                if unit == 'km to mile':
                    output = input_value * 0.6212
                    window['-OUTPUT-'].update(
                        f"{input_value} km are {round(output, 2)} miles.")
                if unit == 'kg to pound':
                    output = input_value * 2.20462
                    window['-OUTPUT-'].update(
                        f"{input_value} kg are {round(output, 2)} pounds.")
                if unit == 'mile to km':
                    output = input_value * 1.6093
                    window['-OUTPUT-'].update(
                        f"{input_value} miles are {round(output, 2)} km.")
                if unit == 'sec to min':
                    output = input_value / 60
                    window['-OUTPUT-'].update(
                        f"{input_value} sec are {round(output, 2)} min.")
            else:
                window['-OUTPUT-'].update('Please enter a number.')

    window.close()


if __name__ == '__main__':
    main()
