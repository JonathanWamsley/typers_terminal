import curses
from curses import wrapper
from abc import ABC, abstractmethod
import types
import sys

class Window:
    '''
    Windows are the medium for communicating input and output to the application/user

    A window has a screen for I/O
        - input displayed to user
            - static_input: displayed before dynamic
                - useful for adding instructions
            - dynamic_input: iterable
                - paragraphs displayed on string
        - user_input
    colors are read from settings


    The Window describes how the user interacts with the window:
        Static Window - User views a page
        Text Window - User sends text as instructed
        Selection Window - User sends selected highlighted row
        Typing Window - User sends keys that are equal the input

    '''
    def __init__(self, stdscr):
        self.stdscr = stdscr
        self.class_input = None
        self.static_message = None
        self.colors = None
        self.user_output = None
        self.setup()

    def setup(self):
        curses.curs_set(0)
        curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
        curses.init_pair(2, curses.COLOR_MAGENTA, curses.COLOR_BLACK)
        self.stdscr.clear()
    
    def cursor_on(self):
        curses.curs_set(2)
  
    def cursor_off(self):
        curses.curs_set(0)

    def move_up(self, key):
        return key == curses.KEY_UP

    def move_down(self, key):
        return key == curses.KEY_DOWN
        
    def move_left(self, key):
        return key == curses.KEY_LEFT

    def move_right(self, key):
        return key == curses.KEY_RIGHT
 
    def enter(self, key):
        return key == curses.KEY_ENTER or key in [10, 13]

    def quit(self, key):
        return key == '\x1b'

    def termination(self, key):
        return key == curses.KEY_F4

    def skip(self, key):
        return key ==  '`'

    def set_static_message(self, static_message):
        self.static_message = static_message
    
    def has_static_message(self):
        if self.static_message:
            return True
        else:
            return False
                
class TextWindow(Window):
    '''
    text window is designed for getting user input

    
    Parameters
        static_message - text shown above where the user inputs text
            - ex. Enter a number: 
        conditions(optional) - A function comparing output

    input = user input
    designed_output = user_input

    use cases
        text - get url, clipboard
        numbers or letters - filters for drills
    '''
    def __init__(self, stdscr, message, conditions = None):
        Window.__init__(self, stdscr)
        self.stdscr = stdscr
        self.message = message
        self.conditions = conditions
        self.output = self.prompt()

    def conditions_met(self, output):
        if isinstance(self.conditions, types.FunctionType):
            return self.conditions(output)
        return True

    def prompt(self):
        ''' Text will only show until screen fills'''
        self.stdscr.clear()
        self.cursor_on()
        shown_output = ''
        output = ''
        eol = False
        max_height, max_width = self.stdscr.getmaxyx()
        y, x = self.stdscr.getyx()
        while True:
            # TODO submit bug to python curses that when an enter is used with
            # get_wch and addstr that the y position does not auto increment
            
            self.stdscr.clrtoeol()
            self.stdscr.refresh()
            if y + 2 > max_height:
                eol = True 
            self.stdscr.addstr(0, 0, self.message+shown_output)
            char = (self.stdscr.get_wch()) # Have to use wch
            if char == curses.KEY_BACKSPACE or char == '\x7f':
                output = output[:-1]
                shown_output = shown_output[:-1]
            elif self.termination(char):
                if self.conditions_met(output):
                    return output
            elif char == '\n' or repr(char) == '\n':
                
                y += 1 # these 2 commits show how if enter is many times, curses does not trigger
                if y + 2 > max_height:
                    eol = True
                if not eol:
                    shown_output += (char)
                output += (char)
                #y, x = self.stdscr.getyx() # and will cause line error
            elif self.quit(char):
                return
            else:
                y, x = self.stdscr.getyx()
                output += (char)
                if not eol:
                    shown_output += (char)
        self.stdscr.clear()


    def get_output(self):
        return self.output


class SelectionWindow(Window):
    '''
    Parameters
        static_message - text shown above where the user inputs text
        selection_functionality
            selection_names = keys - text to be displayed
            values - function or class to be called
        selected_row - int showing current position

    input = a dictionaries with names and a functional response
    output = the selected functional response

    use cases
        file menu
        typing drill selection
        boolean response for paramters
    '''
    def __init__(self, stdscr, static_message = None):
        self.stdscr = stdscr
        self.static_message = static_message
        self.selection_names = []
        self.selection_functionality = {}
        self.selected_row = 0
        self.new_screen = None
        self.setup()


    def print_keys(self):
        '''Displays the selection keys with the highlights selected row'''
        def highlight_row(self):
            self.stdscr.attron(curses.color_pair(1))
            self.stdscr.addstr(row, 0, name)
            self.stdscr.attroff(curses.color_pair(1))

        for row, name in enumerate(self.selection_names):
            if row == self.selected_row:
                highlight_row(self)
            else:
                self.stdscr.addstr(row, 0, name)
        self.stdscr.refresh()

    def prompt_selection_functionality(self):
        '''When enter is pressed on selection name, the corresponding func is triggered 

        A class or a function can be passed and multiple args can be placed in a tuple as
        (class, [args])

        After the class or function is executed, an new screen selection is displayed
        '''
        def get_selection_functionality(self):
            '''Uses the selected row location to retrieve the correspond func'''
            return self.selection_functionality[self.selection_names[self.selected_row]]

        def unpack_args(self, response):
            if isinstance(response, tuple):
                func, args = response
                return func, args
            else:
                return response, None

        def execute_selection_functionality(self, selection_functionality):
            '''Will execute the function or class and pass args'''
            if isinstance(selection_functionality, types.FunctionType):
                selection_functionality(self)
            elif isinstance(selection_functionality, type): # its a class.
                if args:
                    selection_functionality(self.stdscr, args)
                else:
                    selection_functionality(self.stdscr)
            else:
                sys.exit(0)

        def execute_new_screen(self):
            '''After the selection func is done, the end screen will appear'''
            if self.new_screen:
                self.new_screen(self.stdscr)
            else:
                sys.exit(0)

        selection_functionality_packed = get_selection_functionality(self)
        selection_functionality, args = unpack_args(self, selection_functionality_packed)
        execute_selection_functionality(self, selection_functionality)
        execute_new_screen(self)

    def move_up(self, key):
        return self.selected_row > 0 and (key == curses.KEY_UP or key == ord('k'))

    def move_down(self, key):
        return self.selected_row < len(self.selection_names) - 1 and (key == curses.KEY_DOWN or key == ord('y'))
 
    def enter(self, key):
        return key == curses.KEY_ENTER or key in [10, 13]

    def display_screen(self):
        self.print_keys()
        while True:
            key = self.stdscr.getch()
            if self.move_up(key):
                self.selected_row -= 1
            elif self.move_down(key):
                self.selected_row += 1
            elif self.enter(key):
                self.prompt_selection_functionality()
            self.print_keys()
    
    def set_selection_functionality(self, functionalities):
        self.selection_functionality = functionalities
        self.selection_names = list(self.selection_functionality.keys())

    def set_new_screen(self, new_selection):
        self.new_screen = new_selection


class StaticWindow(Window):
    '''
    Parameters
        fitted_paragraphs

    input = fitted_paragraphs
    designed_output = none

    use cases
        statistics
        about page
    '''
    def __init__(self, stdscr, fitted_paragraphs):
        self.stdscr = stdscr
        self.fitted_paragraphs = fitted_paragraphs
        self.setup()
        self.display_fitted_paragraphs()

    def display_fitted_paragraphs(self):
        char = self.stdscr.get_wch()
        while char != self.quit:
            for fitted_paragraph in fitted_paragraphs:
                x = 0
                y = 0
                self.stdscr.move(x, y)
                for fitted_line in fitted_paragraph:
                    self.stdscr.addstr(y, x, fitted_line)
                    x = 0
                    y += 1
                char = self.stdscr.get_wch()
                while char != self.move_right or char != quit:
                    self.stdscr.get_wch()
                self.stdscr.clear()


class TypeTextWindow:

    '''
    Parameters
        fitted paragraphs
        triggers - [exit early, skip symbol]
        assertion -  condition for type, or len of output text

    navigateable pages with arrow keys

    input = fitted paragraphs/user typing those paragraphs
    designed_output = log of typing times

    use cases
        sponge typer, typer

    '''
    def __init__(self):
        pass
