import curses
import sys
import os
import types

from application.text_displayer import TextDisplayer
from application.typing_drills import TypingDrills
from application.speed_reading_displayer import SpeedReadingDisplayer
from application.sponge_typing_displayer import SpongeTypingDisplayer


'''The application contains only menus with a corresponding functionalities.
Each application menu inherits from menu
Each menu calls on another menu, class or func
'''

class Menu:
    '''This class creates an interface menus that can be navigated with curses'''
    def __init__(self, stdscr):
        '''The menu stores
           menu  (list)
           menu dictionary mapping menu names to menu functionalities (dict)
           location of the cursor (int)
        '''
        self.stdscr = stdscr
        self.menu_names = []
        self.menu_functionality = {}
        self.selected_menu_row = 0
        self.end_screen = None
        self.setup()

    def setup(self):
        curses.curs_set(0)
        curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
        curses.init_pair(2, curses.COLOR_MAGENTA, curses.COLOR_BLACK)
        self.stdscr.clear()

    def print_menu(self):
        '''Displays the menu items with the highlights selected menu row'''
        def highlight_row(self):
            self.stdscr.attron(curses.color_pair(1))
            self.stdscr.addstr(row, 0, menu_name)
            self.stdscr.attroff(curses.color_pair(1))

        for row, menu_name in enumerate(self.menu_names):
            if row == self.selected_menu_row:
                highlight_row(self)
            else:
                self.stdscr.addstr(row, 0, menu_name)
        self.stdscr.refresh()

    def prompt_menu_functionality(self):
        '''When enter is selected on menu name, the corresponding menu func is triggered 

        A class or a function can be passed and multiple args can be placed in a tuple as
        (class, [args])

        After the class or function is executed, an end screen menu is displayed
        '''
        def get_menu_functionality(self):
            '''Uses the selected menu row location to retrieve the correspond menu func'''
            return self.menu_functionality[self.menu_names[self.selected_menu_row]]

        def unpack_args(self, response):
            if isinstance(response, tuple):
                func, args = response
                return func, args
            else:
                return response, None

        def execute_menu_functionality(self, menu_functionality):
            '''Will execute the function or class and pass args'''
            if isinstance(menu_functionality, types.FunctionType):
                menu_functionality(self)
            elif isinstance(menu_functionality, type): # its a class.
                if args:
                    menu_functionality(self.stdscr, args)
                else:
                    menu_functionality(self.stdscr)
            else:
                sys.exit(0)

        def execute_end_screen(self):
            '''After the menu func is done, the end screen will appear'''
            if self.end_screen:
                self.end_screen(self.stdscr)
            else:
                sys.exit(0)

        menu_functionality_packed = get_menu_functionality(self)
        menu_functionality, args = unpack_args(self, menu_functionality_packed)
        execute_menu_functionality(self, menu_functionality)
        execute_end_screen(self)

    def move_up(self, key):
        return self.selected_menu_row > 0 and (key == curses.KEY_UP or key == ord('k'))

    def move_down(self, key):
        return self.selected_menu_row < len(self.menu_names) - 1 and (key == curses.KEY_DOWN or key == ord('y'))
 
    def enter(self, key):
        return key == curses.KEY_ENTER or key in [10, 13]

    def display_screen(self):
        self.print_menu()
        while True:
            key = self.stdscr.getch()
            if self.move_up(key):
                self.selected_menu_row -= 1
            elif self.move_down(key):
                self.selected_menu_row += 1
            elif self.enter(key):
                self.prompt_menu_functionality()
            self.print_menu()
    
    def set_menu_functionality(self, functionalities):
        self.menu_functionality = functionalities
        self.menu_names = list(self.menu_functionality.keys())

    def set_end_screen(self, menu):
        self.end_screen = menu

class Start(Menu):
    '''The opening menu where the program starts
    as well as a often being used as an end screen'''
    def __init__(self, stdscr):
        Menu.__init__(self, stdscr)
        self.package_functions()
        self.display_screen()

    def package_functions(self):
        
        def exit(self):
            sys.exit(0)

        func = {
            'Sponge Typing': SpongeTyping,
            'Typing': Typing,
            'Speed Reading': SpeedReading,
            'View Statistics': exit,
            'Settings': Settings,
            'Exit': exit,
        }
        self.set_menu_functionality(func)


class Typing(Menu):
    
    def __init__(self, stdscr):
        Menu.__init__(self, stdscr)
        self.package_functions()
        self.display_screen()

    def package_functions(self):
        
        def about(self):
            pass

        func = {
            'Drills': Drills,
            'Submit Text': SubmitText,
            'Return To Menu': Start,
        }
        self.set_menu_functionality(func)


class Drills(Menu):
    
    def __init__(self, stdscr):
        Menu.__init__(self, stdscr)
        self.stdscr = stdscr
        self.package_functions()
        self.display_screen()

    def package_functions(self):

        func = {
            'Bigraphs': (DrillsWordList, 'bigraphs'),
            'Trigraphs': (DrillsWordList, 'trigraphs'),
            'Words': (DrillsWordList, 'words'),
            'Return To Typing': Typing,
        }
        self.set_menu_functionality(func)


class DrillsWordList(Menu):
    def __init__(self, stdscr, drill_type = 'words'):
        Menu.__init__(self, stdscr)
        self.stdscr = stdscr
        self.drill_type = drill_type
        self.package_functions()
        self.display_screen()

    def package_functions(self):

        # TODO codesmell, should put functions in separate file to be called
        # TODO codesmell and UI smell, menus are called to get a single parameter
        def select_word_list(self):
            file_mappings = {}
            for file in os.listdir("../data/"):
                if file.endswith(".txt"):
                    file_mappings[file] = (DrillsWordAmount, (self.drill_type, file))

            file_mappings['Return To Menu'] = Drills
            return file_mappings
        func = select_word_list(self)
        self.set_menu_functionality(func)


class DrillsWordAmount(Menu):
    def __init__(self, stdscr, drill_type = 'words'):
        Menu.__init__(self, stdscr)
        self.stdscr = stdscr
        self.drill_type = drill_type
        self.package_functions()
        self.display_screen()

    def __init__(self, stdscr, args):
        Menu.__init__(self, stdscr)
        self.stdscr = stdscr
        self.drill_type,  self.file = args
        self.package_functions()
        self.display_screen()

    def package_functions(self):

        def prompt_word_amount(self):
            amount = get_word_amount(self)
            return (DrillsWordFilter, (self.drill_type, self.file, amount))

        def get_word_amount(self):
            self.stdscr.clear()
            amount = ''
            curses.curs_set(2)
            while True:
                self.stdscr.addstr(0, 0, 'Enter The Amount Of Words To Type: ')
                self.stdscr.clrtoeol()
                self.stdscr.addstr(amount)
                char = self.stdscr.get_wch()
                if char.isprintable():
                    amount += char
                elif char == curses.KEY_BACKSPACE or char == '\x7f':
                    amount = amount[:-1]
                elif char == curses.KEY_ENTER or char == '\n':
                    try:
                        amount = int(amount)
                    except:
                        amount = ''
                    else:
                        break
            self.stdscr.clear()
            return int(amount)


        func = {
            'Words Amount': prompt_word_amount(self),
            'Return To Typing': Typing,
        }

        self.set_menu_functionality(func)


class DrillsWordFilter(Menu):
    def __init__(self, stdscr, args):
        Menu.__init__(self, stdscr)
        self.stdscr = stdscr
        self.drill_type, self.file, self.word_amount = args
        self.package_functions()
        self.display_screen()

    def package_functions(self):

        def display_words(self):
            filtered_letters = get_filter_letters(self)
            displayed_words = TypingDrills(self.drill_type, self.file, self.word_amount, filtered_letters)
            return (TextDisplayer, ' '.join(displayed_words.words))

        def get_filter_letters(self):
            self.stdscr.clear()
            filter_letters = ''
            curses.curs_set(2)
            while True:
                self.stdscr.addstr(0, 0, 'Enter The Starting Letters To Use Or Enter Blank For All: ')
                self.stdscr.clrtoeol()
                self.stdscr.addstr(filter_letters)
                char = self.stdscr.get_wch()
                if char.isprintable():
                    filter_letters += char
                elif char == curses.KEY_BACKSPACE or char == '\x7f':
                    filter_letters = filter_letters[:-1]
                elif char == curses.KEY_ENTER or char == '\n':
                    break
            self.stdscr.clear()
            return filter_letters

        def about(self):
            pass

        func = {
            'Filtered Words': display_words(self),
            'Return To Typing': Typing,
        }
        self.set_end_screen(Start)
        self.set_menu_functionality(func)


class SubmitText(Menu):
    
    def __init__(self, stdscr):
        Menu.__init__(self, stdscr)
        self.stdscr = stdscr
        self.package_functions()
        self.display_screen()

    def package_functions(self):

        def about(self):
            pass

        func = {
            'Enter URL': (TextDisplayer, 'url'),
            'Paste Clipboard':  (TextDisplayer, 'clipboard'),
            'Return To Typing': Typing,
        }
        self.set_end_screen(Start)
        self.set_menu_functionality(func)

class SpeedReading(Menu):
    
    def __init__(self, stdscr):
        Menu.__init__(self, stdscr)
        self.stdscr = stdscr
        self.package_functions()
        self.display_screen()

    def package_functions(self):

        def about(self):
            pass

        func = {
            'Enter URL': (SpeedReadingDisplayer, 'url'),
            'Paste Clipboard':  (SpeedReadingDisplayer, 'clipboard'),
            'Return To Menu': Start,
        }
        self.set_end_screen(Start)
        self.set_menu_functionality(func)

        
class SpongeTyping(Menu):
    
    def __init__(self, stdscr):
        Menu.__init__(self, stdscr)
        self.stdscr = stdscr
        self.package_functions()
        self.display_screen()

    def package_functions(self):

        def about(self):
            pass

        func = {
            'Enter URL': (SpongeTypingDisplayer, 'url'),
            'Paste Clipboard':  (SpongeTypingDisplayer, 'clipboard'),
            'Return To Menu': Start,
        }
        self.set_end_screen(Start)
        self.set_menu_functionality(func)

class Settings(Menu):

    def __init__(self, stdscr):
        Menu.__init__(self, stdscr)
        self.package_functions()
        self.display_screen()

    def package_functions(self):
        
        def about(self):
            pass

        func = {
            'Change Key Configurations': about,
            'Restore Default Key Configurations': about,
            'Change Screen Colors': about,
            'Return To Menu': Start,
        }
        self.set_menu_functionality(func)
