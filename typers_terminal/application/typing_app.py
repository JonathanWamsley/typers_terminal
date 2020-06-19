import curses
from timeit import default_timer as timer
from applications.utilities import get_text, fit_text
from applications.typing_drills import get_typing_drill


class TypingApp:
    def __init__(self, stdscr, input_type):
        '''Focuses on the typeing
        3 input forms
        speed drills
        url
        clipboard
        '''
        self.stdscr = stdscr
        self.input_type = input_type
        self.text = self._get_text()
        self.setup()
        self.draw()

    def setup(self):
        self.stdscr.clear()
        curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
        self.stdscr.attron(curses.color_pair(1))
        curses.curs_set(2)

    def _get_text(self):
        if self.input_type == 'drill':
            drill = get_typing_drill()
        elif self.input_type == 'url' or self.input_type == 'clipboard':
            text = get_text(self.input_type)
        return text

    def _proccess_text(self, text: str) -> list[list[str]]:
        # NlP first? maybe a trigger option
        max_height, max_width = self.stdscr.getmaxyx()
        return fit_text(text, max_height, max_width)


    def type_text(self):
        text = _get_text()
        proccessed_text = _proccess_text(text)
        #typing_log = display_text(proccessed_text)

