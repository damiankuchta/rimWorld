from resources import resources, building_resources
from config import actions
from buildings.buildings import buildings
import PySimpleGUI as sg


class GUI:
    def __init__(self, colony):
        self._update_data(colony)
        self.main_window = self._create_main_window()

    def _create_main_window(self):
        sg.theme('DarkAmber')  # Add a touch of color
        # All the stuff inside your window.
        layout = [[sg.Table(values=self.resources,
                            hide_vertical_scroll=True,
                            headings=['Resources', 'Amount'], key='-RESOURCES-'), ],
                  [sg.Table(values=self.colonists,
                            hide_vertical_scroll=True,
                            headings=['Colonist', 'Actions', 'Max actions'], key='-COLONIST-'),
                   *[sg.Button(b, key='{}'.format(b)) for b in actions]],
                  [sg.Table(values=self.buildings_list,
                            hide_vertical_scroll=True,
                            headings=['Buildings'], key='-BUILDINGS-'), ],
                  [sg.Button('Next round')],

                  ]

        # Create the Window
        return sg.Window('RimWorld board game', layout)

    def start(self, colony):
        # Event Loop to process "events" and get the "values" of the inputs
        while True:  # Event Loop
            event, values = self.main_window.read()
            print(event, values)
            if event == sg.WIN_CLOSED or event == 'Exit':
                break
            if event in actions:
                if len(values['-COLONIST-']) == 1:
                    new_window = getattr(self, "_" + event + "_window", 'invalid')

                    if new_window != "invalid":
                        new_window(colony, colony.colonists[values['-COLONIST-'][0]])
                    else:
                        colony.colonists[values['-COLONIST-'][0]].take_action(colony, event)

                    self._update_window(colony)
                else:
                    sg.popup_error('Chose one colonist!')
            if event == 'Next round':
                colony.reset()
                self._update_window(colony)

        self.main_window.close()

    def _build_window(self, colony, colonist):
        layout = [[sg.Table(values=self.to_build_buildings_list, hide_vertical_scroll=True,
                            headings=['Name', 'Action cost', *[b for b in building_resources]], key='-BUILDINGS-'),
                   sg.Table(values=self.resources, hide_vertical_scroll=True,
                            headings=['Resources', 'Amount'], key='-RESOURCES-')],
                  [sg.Button('Build')]]
        window = sg.Window("Building Window", layout, modal=True)

        while True:  # Event Loop
            event, values = window.read()
            print(event, values)
            if event == sg.WIN_CLOSED or event == 'Exit':
                break
            if event == "Build":
                if len(values['-BUILDINGS-']) == 1 and len(values['-RESOURCES-']) == 1:
                    is_sucesfull = colonist.take_action(colony,
                                                        action="build",
                                                        build=self.to_build_buildings_list[values['-BUILDINGS-'][0]][0],
                                                        resources=resources[values['-RESOURCES-'][0]])
                    if is_sucesfull[0] is False:
                        sg.popup_error(is_sucesfull[1])
                else:
                    sg.popup_error("pick one building and one type or resources!")
        window.close()

    def _update_window(self, colony):
        self._update_data(colony)
        self.main_window['-RESOURCES-'].update(self.resources)
        self.main_window['-COLONIST-'].update(self.colonists)
        self.main_window['-BUILDINGS-'].update(self.buildings_list)

    def _update_data(self, colony):
        self.colonists = [[c.name, c.active_actions, c.max_actions] for c in colony.colonists]
        self.resources = [[r, colony.resources[r]] for r in resources]
        self.buildings_list = [r for r in colony.buildings]
        self.to_build_buildings_list = [[buildings[b].name, buildings[b].building_action_cost,
                                         *[buildings[b].cost[c] for c in buildings[b].cost.keys()]] for b in
                                        buildings.keys()]
