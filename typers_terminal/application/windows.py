import curses
from curses import wrapper


class Window:
    '''
    make sure text stays on screen
    creates navigateable pages
    applies user settings
    '''
    def __init__(self, stdscr):
        pass


class GetTextWindow:
    '''
    Parameters
        message - text shown above where the user inputs text
        trigger - how to confirm message
        assertion -  condition for type, or len of output text

    input = user input
    designed_output = user_input

    use cases
        text - get url, clipboard
        numbers or letters - filters for drills
    '''
    def __init__(self, stdscr, message, trigger, assertion = None):
        self.stdscr = stdscr
        self.message = message
        self.trigger = trigger
        self.assertion = None # can limit text type(int,str), can limit 1 value
        self.output = self.prompt()
        

    def prompt(self):
        self.stdscr.clear()
        curses.curs_set(0)
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
                shown_output = output[:-1]
            elif char == self.trigger:
                return output
            elif char == '\n' or repr(char) == '\n':
                
                y += 1 # these 2 commits show how if enter is many times, curses does not trigger
                if y + 2 > max_height:
                    eol = True
                if not eol:
                    shown_output += (char)
                output += (char)
                #y, x = self.stdscr.getyx() # and will cause line error
            else:
                y, x = self.stdscr.getyx()
                output += (char)
                if not eol:
                    shown_output += (char)
        self.stdscr.clear()
        return output

    def get_output(self):
        return self.output


class GetSelectionWindow:
    '''
    Parameters
        message - text shown above where the user inputs text
        trigger - how to confirm message

    input = a dictionaries with names and a functional response
    output = the selected functional response

    use cases
        file menu
        typing drill selection
        boolean response for paramters
    '''
    def __init__(self, stdscr, message, Selection):
        self.stdscr = stdscr
        self.message = message
        self.trigger = trigger
        self.output = self.prompt()


class StaticWindow:
    '''
    Parameters
        fitted_paragraphs
        trigger - trigger to exit

    input = fitted_paragraphs
    designed_output = none

    use cases
        statistics
        about page
    '''
    def __init__(self):
        pass

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
