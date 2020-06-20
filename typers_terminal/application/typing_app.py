import curses
from timeit import default_timer as timer
from application.utilities import get_text, fit_text
#from application.typing_drills import get_typing_drill


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
        self.type_text()

    def setup(self):
        self.stdscr.clear()
        curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
        self.stdscr.attron(curses.color_pair(1))
        curses.curs_set(2)

    def _get_text(self):
        if self.input_type == 'drill':
            #text = get_typing_drill()
            pass
        elif self.input_type == 'url' or self.input_type == 'clipboard':
            text = get_text(self.stdscr, self.input_type)
        return text

    def _process_text(self, text):
        # NlP first? maybe a trigger option
        max_height, max_width = self.stdscr.getmaxyx()
        return fit_text(text, max_height, max_width)

    def type_processed_text(self, paragraphs):
        char_time_log = []
        word_time_log = []
        for paragraph in paragraphs:
            self.stdscr.move(0, 0)
            self.stdscr.clear()
            x = 0
            y = 0

            for lines in paragraph:
                words = ' '.join(lines)
                self.stdscr.addstr(y, x, words)
                x = 0
                y += 2

            self.stdscr.move(0, 0)
            x = 0
            y = 0

            for lines in paragraph:
                words = ' '.join(lines)
                self.stdscr.addstr(y, x, words)
                self.stdscr.move(y, x)

                letters = ''
                good_accuracy_word = []
                # input starts here
                for idx, letter in enumerate(words):
                    good_accuracy = True
                    char = self.stdscr.get_wch()
                    if idx == 0:
                        char_len = 1
                        start_word = timer()
                    start_time = timer()
                    while char != letter:
                        char = self.stdscr.get_wch()
                        if char == '`':
                            # an autoskip for special characters that can not be entered
                            char = letter
                        if char == '\x1b':
                            return char_time_log, word_time_log
                        good_accuracy = False
                    end_time = timer()
                    delta = end_time - start_time
                    letters += letter
                    good_accuracy_word.append(good_accuracy)
                    char_time_log.append((char, delta, good_accuracy))
                    if char == ' ' or idx == len(words) - 1:
                        end_word = timer()
                        delta_word = end_word - start_word
                        wpm = str(round((60 / (delta_word / char_len))/5))
                        if char_len > 2:
                            self.stdscr.addstr(y+1, x-char_len + 1, wpm, curses.color_pair(2))
                        char_len = 1
                        word_time_log.append((letters, wpm, all(good_accuracy_word)))
                        letters = ''
                        good_accuracy_word = []
                        start_word = timer()
                    else:
                        char_len += 1
                        

                    if x + 1 < len(words):  
                        x += 1
                    else:
                        x = 0
                    self.stdscr.move(y, x)
                x = 0
                y += 2
        return char_time_log, word_time_log



    def display_word_stats(self, word_time_log):
        char = self.stdscr.get_wch()
        self.stdscr.clear()
        curses.curs_set(0)
        time_sorted = sorted(word_time_log, key = lambda x: int(x[1]))
        correct_words = [word for word in word_time_log if word[2]]
        correct_words_sorted = sorted(correct_words, key = lambda x: int(x[1]))
        fastest_words = time_sorted[-5:]
        slowest_words = time_sorted[:5]
        slowest_correct_words = correct_words_sorted[:5]
        average_wpm = sum([int(time) for word, time, accuracy in time_sorted])/len(time_sorted)
        average_accuracy = sum([accuracy for word, time, accuracy in time_sorted])/len(time_sorted)
        average_stats = f'Average wpm: {str(average_wpm)},  Accuracy: {str(average_accuracy)}'
        fastest_words_stats = f'Fastest Words: {str(fastest_words)}'
        slowest_words_stats = f'Slowest Words: {str(slowest_words)}'
        slowest_correct_words_stats = f'Slowest Correct Words: {str(slowest_correct_words)}'
        self.stdscr.move(0, 0)
        self.stdscr.addstr(0, 0, average_stats)
        self.stdscr.addstr(1, 0, fastest_words_stats)
        self.stdscr.addstr(2, 0, slowest_words_stats)
        self.stdscr.addstr(3, 0, slowest_correct_words_stats)
        char = self.stdscr.get_wch()
        self.stdscr.clear()


    def type_text(self):
        text = self._get_text()
        processed_text = self._process_text(text)
        char_time_log, word_time_log  = self.type_processed_text(processed_text)
        self.display_word_stats(word_time_log)

