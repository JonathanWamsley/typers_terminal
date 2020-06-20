import curses
import sys
import os
import types

from application.text_displayer import TextDisplayer
from application.typing_drills import TypingDrills
from application.speed_reading_displayer import SpeedReadingDisplayer
from application.sponge_typing_displayer import SpongeTypingDisplayer
from application.windows import SelectionWindow
from application.typing_app import TypingApp

'''The application contains only a selection menus with a corresponding functionalities.
Each application menu inherits from menu
Each menu calls on another menu, class or func
'''

class Start(SelectionWindow):
    '''The opening menu where the program starts
    as well as a often being used as an end screen'''
    def __init__(self, stdscr):
        SelectionWindow.__init__(self, stdscr)
        self.package_functions()
        self.display_screen()

    def package_functions(self):
        
        def exit(self):
            sys.exit(0)

        func = {
            'Typing V2': Typing2,
            'Sponge Typing': SpongeTyping,
            'Typing': Typing,
            'Speed Reading': SpeedReading,
            'View Statistics': exit,
            'Settings': Settings,
            'Exit': exit,
        }
        self.set_selection_functionality(func)


class Typing(SelectionWindow):
    
    def __init__(self, stdscr):
        SelectionWindow.__init__(self, stdscr)
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
        self.set_selection_functionality(func)

class Typing2(SelectionWindow):
    
    def __init__(self, stdscr):
        SelectionWindow.__init__(self, stdscr)
        self.package_functions()
        self.display_screen()

    def package_functions(self):
        
        def about(self):
            pass

        func = {
            'Drills': (TypingApp, 'clipboard'),
            'Submit Text': SubmitText,
            'Return To Menu': Start,
        }
        self.set_selection_functionality(func)


class Drills(SelectionWindow):
    
    def __init__(self, stdscr):
        SelectionWindow.__init__(self, stdscr)
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
        self.set_selection_functionality(func)


class DrillsWordList(SelectionWindow):
    def __init__(self, stdscr, drill_type = 'words'):
        SelectionWindow.__init__(self, stdscr)
        self.stdscr = stdscr
        self.drill_type = drill_type
        self.package_functions()
        self.display_screen()

    def package_functions(self):

        # TODO codesmell, should put functions in separate file to be called
        # TODO codesmell and UI smell, SelectionWindows are called to get a single parameter
        def select_word_list(self):
            file_mappings = {}
            for file in os.listdir("../data/"):
                if file.endswith(".txt"):
                    file_mappings[file] = (DrillsWordAmount, (self.drill_type, file))

            file_mappings['Return To Menu'] = Drills
            return file_mappings
        func = select_word_list(self)
        self.set_selection_functionality(func)


class DrillsWordAmount(SelectionWindow):
    def __init__(self, stdscr, drill_type = 'words'):
        SelectionWindow.__init__(self, stdscr)
        self.stdscr = stdscr
        self.drill_type = drill_type
        self.package_functions()
        self.display_screen()

    def __init__(self, stdscr, args):
        SelectionWindow.__init__(self, stdscr)
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

        self.set_selection_functionality(func)


class DrillsWordFilter(SelectionWindow):
    def __init__(self, stdscr, args):
        SelectionWindow.__init__(self, stdscr)
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
        self.set_new_screen(Start)
        self.set_selection_functionality(func)


class SubmitText(SelectionWindow):
    
    def __init__(self, stdscr):
        SelectionWindow.__init__(self, stdscr)
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
        self.set_new_screen(Start)
        self.set_selection_functionality(func)

class SpeedReading(SelectionWindow):
    
    def __init__(self, stdscr):
        SelectionWindow.__init__(self, stdscr)
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
        self.set_new_screen(Start)
        self.set_selection_functionality(func)

        
class SpongeTyping(SelectionWindow):
    
    def __init__(self, stdscr):
        SelectionWindow.__init__(self, stdscr)
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
        self.set_new_screen(Start)
        self.set_selection_functionality(func)

class Settings(SelectionWindow):

    def __init__(self, stdscr):
        SelectionWindow.__init__(self, stdscr)
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
        self.set_selection_functionality(func)
