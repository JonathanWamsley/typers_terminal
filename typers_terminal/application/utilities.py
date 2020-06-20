import curses
from curses import wrapper
from bs4 import BeautifulSoup
import requests

from application.windows import TextWindow


'''This utilities.py holds functions used in the *app.py files

Main functions are:
    get_text
    process_text
    analyze_text
'''


def get_text(stdscr, input_type):
    '''opens either url or clipboard text prompt'''

    def get_text_from_url(stdscr):
        url = TextWindow(stdscr, message = 'Enter a URL and F4 when done: ').get_output()
        text = scrape_url(url)
        return text

    def scrape_url(url):
        text = ''
        if url:
            headers = requests.utils.default_headers()
            headers.update({ 'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'})
            req = requests.get(url, headers)
            soup = BeautifulSoup(req.content, 'html.parser')
            wanted_tags = ['p',  'li', 'ul']
            for header in soup.find_all(['h1','h2','h3']):
                # a \h is used to indicate header
                text += header.get_text() + '\h' + '\n'
                for elem in header.next_elements:
                    if elem.name and elem.name.startswith('h'):
                        break
                    if any([True for tag in wanted_tags if tag == elem.name]):
                        text += elem.get_text() + '\n'
        return text

    def get_text_from_clipboard(stdscr):
        return TextWindow(stdscr, message = 'Paste Clipboard and F4 when done: ').get_output()

    if input_type == 'url':
        text = get_text_from_url(stdscr)
    elif input_type == 'clipboard':
        text = get_text_from_clipboard(stdscr)
    return text


def fit_text(doc, max_line_height, max_char_width):
    '''Takes in a raw text and applies transforms so the text can be displayed
    - format text to screen
        - format width
        - format hight

    - output
        - screens of lines or words: screens[lines[words]]
    '''
    def divide_chunks_by_width(paragraph, max_char_width):
        line = ''
        words = paragraph.split()
        header = False
        if paragraph[-2:] == '\h':
            header = True
        for idx, word in enumerate(words):
            if len(line) + len(word) + 1 < max_char_width:
                line += word + ' '
            else:
                if header:
                    line += '\h'
                yield line
                line = word + ' '
            if idx == len(words) - 1:
                yield line

    def divide_chunks_by_height(paragraphs, max_line_height):
        if len(paragraphs) < max_line_height:
            yield paragraphs
        else:
            for idx in range(0, len(paragraphs), max_line_height): 
                yield paragraphs[idx:idx + max_line_height] 

    paragraphs = doc.split('\n')
    paragraph_fitted_on_screen = []
    for paragraph in paragraphs:
        paragraph_by_width = [*divide_chunks_by_width(paragraph, max_char_width)]
        paragraph_fitted_on_screen.append([*divide_chunks_by_height(paragraph_by_width, (max_line_height))])
    return paragraph_fitted_on_screen


def apply_nlp(doc):
    pass

def analyze_text():
    pass


def main(stdscr):
    text = TextWindow(stdscr, 'clipboard')

if __name__ == "__main__":
    wrapper(main)
