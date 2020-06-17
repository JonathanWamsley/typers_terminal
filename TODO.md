# TODO Goals

# Refactoring
- annotations
- cleaner code
- separate stats from text displayer

# features
- add a sql lite database with
    - word, # correctly typed, max wpm, average wpm, etc
- do NLP to color code parts of speech in words
- do speed reading section
    - add amount off character spacing to display words
- add normal coloring and nightmode coloring in settings

# bugs
- wrap text around screen for the stats
- error check on max elements to display, should be done in menu
- fix drill menu sequence prompts
- menus are not function if after typing/speed reading ends with esc


### Setting up for success
- Project's goal and approach to acheive that goal
    - ____ is A open source terminal based typing and speed reading application to accelarate learning
    - It can be used to increase the rate of comprehension of books, articles, documentaion, etc.

- Why make Typers_Terminal?
    - To learn faster by speed reading content from any site and type the content

- What similar products are out?
    - For typing
        - TypeRacer, 10fastfingers, nitrotype
        - They all type random words or quoets
        - Some have a section to post text, but there is a cap on the amount of words and they are badly formated
    - For speed reading
        - spreeder, spritz, accelareader
        - they present all words to process at equal speed
        - When people normally type, they spend more time on content words(nouns and verbs), not the same amount of time
        - https://www.youtube.com/watch?v=JL4WMHyUhdc
        - regression is normal, and you should be able to go back and forth

- contribution instructions

- license

- README

- Organization
    - How the project is structured
    - where everything lives
    - how the code is written
    - kinds of tests required


### Speed Reading
- Speed Reading
    - Enter URL
    - Enter Clipboard
    - Return To Menu

- Display Speed Reading
    - Features
        - Pause Space
        - Go back 10 words, i
        - Go forward 10 words, o
        - Increase speed, Up Arrow
        - Increase char space, Right Arrow
        - Decrease speed, Down Arrow
        - Decrease char space, Left arrow

- bugs
    - there is an increase in word speed as you push a button
    - menu after it is finished is not working



### keywords
- terminal
- python
- note comprehension
- speed reading
- speed typing
- fast learning

### Possible Names

name can come from
- acronyms
- mash-ups
- Get inspiration from mythology and literature


Efficiently Learning



good words to describe a way to gain knowledge quickly and effectively,

synthesis of typing and writing like you said

needs to have type, learn

- retentive
- accelerate
- attaint
- acquisition
- agile

- accelalearn (there is an accelareader, which may be why I thought of that)
- consolitype /consolatype
- typalize
- typegration
- typefuse
- effectatype






### Hidden rules

'`' will skip letter when pressed twice
esc will stop the program
there is a hidden pause at the beginning of the new line if you want to take a break and pause
words are added until there is a space at the end
them and them. and them? are all considered different

### Though process

The goal is not to read quickly but to learn quickly.  
If you are going faster than you comprehend, you are creating unnecessary knowledge gaps

For speed reading
    - have all the headers shown first slowly in a green  
    - have the nouns in blue
    - verbs in red
    - exceptions in magenta

have the header shown with slight pause, followed by the words. Then at the end, show the header one more time.  

BeeLine is a company that color codes lines at a gradient to make your eye wonder less
https://www.beelinereader.com/

Can change the background color on the current line


What if speed reading is merged with typing?

You instead read a line and are prompted to type only the nouns, verbs and exceptions?

At the end, provide a short summary while the main headers are shown. Maybe over look the first and last paragraph again?  

Curses is designed to create text editors, so there is no reason why all this information can not be displayed in an editor

to increase comprehension:  
- scan over the headers slowly
- prompt user why they want to learn this
- show paragraphs of words with important terms colored and to proceed you type them


- merging learn process
Consolatype

Consolitype
- integrating reading, typing and comprehending techniques for efficient learning.

### Vision

User submits text

- URL is parsed creating tags
- NLP  also creates tags

- headers are shown
- text is displayed in paragraphs on screen and creates a new paragraph is larger 
- current line is highlighted or wpm is shown?
- important words are typed out

- You can move up and down lines or left and right pages
- stats are summarized and a good job meter comparing average

- summarize based on using the keywords in the headers

