from curses import wrapper
from application.app import Start


def main(stdscr):
    Start(stdscr)

if __name__ == "__main__":
    wrapper(main)
