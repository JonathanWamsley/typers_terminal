# TODO Goals

# Refactoring
- annotations
- cleaner code

# features
- add a sql database with
    - word, # correctly typed, max wpm, average wpm, etc
- add normal coloring and nightmode coloring in settings

# bugs
- wrap text around screen for the stats
- fix drill menu sequence prompts(will get ride of it soon)


### Setting up for success
- Project's goal and approach to achieve that goal
    - Typers_Terminal is A open source terminal based typing and speed reading application to accelerate learning
    - It can be used to increase the rate of comprehension of books, articles, documentation, etc.

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
- acquisition agile

- accelalearn (there is an accelareader, which may be why I thought of that)
- consolitype /consolatype
- typalize
- typegration
- typefuse
- effectatype


- consolitype
- spongetyper

- transcribe
- typscribe
- scribe
- rescribe
- 

Organization Name

SpongeLearners

product, SpongeTyper





### Hidden rules to be address or tell users

feature - '`' will skip letter when pressed twice
feature - esc will stop the program
intentional if you want to break -there is a hidden pause at the beginning of the new line if you want to take a break and pause


### Thought process

The goal is not to read quickly but to learn quickly.  
If you are going faster than you comprehend, you are creating unnecessary knowledge gaps


BeeLine is a company that color codes lines at a gradient to make your eye wonder less
https://www.beelinereader.com/

Can change the background color on the current line


to increase comprehension:  
- scan over the headers slowly
- prompt user why they want to learn this
- show paragraphs of words with important terms colored and to proceed you type them


- merging learn process
Consolatype

- integrating reading, typing and comprehending techniques for efficient learning.


#### Sponge Typer

- what
    Sponge typer is a tool for accelerating the learning process of text ingestion.
- how
    Sponge typer is an effective learning tool because it integrates reading, typing and comprehension techniques
- who
    Sponge typer is for anyone that wants to learn from text documents efficiently
- where
    Sponge typer online browser or downloadable exe file ?
- when
    Sponge typer will be open source with a GNU licence ready by July 2020?
- why
    Sponge typer is a novel way of learning detailed documents faster, saving time and increasing comprehension(back this claim up)

### NLTK or Spacy

 can build chatbots, automatic summarizers, and entity extraction engines with either of these libraries.

 NLTK was created to support education and help students explore ideas.

SpaCy, on the other hand, is the way to go for app developers. It provides the fastest and most accurate syntactic analysis of any NLP library released to date. It also offers access to larger word vectors that are easier to customize. For an app builder mindset that prioritizes getting features done, spaCy would be the better choice.

Winner, Spacy

### Spacy installation

https://spacy.io/usage/

Recommended to download in a virtual environment

pip install -U spacy
python -m spacy download en

### Tokenize

Instead of using python's split(), Tokenization can be used which is a more robust way to split text based off of word and punctuation context.

Can identify parts of speech for words

### Entities

For nouns, can I identify more into about it.

Very useful for Names or Money or some quantity

Can make an option to instead of spelling the name, can spell the entity type if the user feels the specifics are not important

Could also show all entities with high frequency at the end with relations to other nouns or verbs?

###  POS problem

Change words like You'll change to You will and highlight the will


### Hosting

Launching Docker container on mybinder.org like spacy does for its interactive tutorials. This can fit into websites easily


# Typers Terminal Formatting

# Interface Menu
- sponge typing
    - enter url
    - enter clipboard
- typing
    - typing drills
        - typing exercise
            - predefined drills
        - custom exercise
            - custom selections
    - enter url
    - enter clipboard
- reading
    - enter url
    - enter clipboard
- settings
    - colors
        - dark mode
        - light mode
        - custom
    - pos colors
        - # Later
    
# File Layout
- main.pyi
- Application
    - app.py # Links the applications together with only menus
        - Window(input dictionary, cursor location -> class, func output, final ending screen output)
    - # Interface files
        - typing_app.py
        - reading_app.py
        - sponge_typing_app.py
        - settings.py
            - # later will add statistics
    - # Windows classes
        - Create Get input Window(user input, text output)
            - Get Text
                - url, clipboard
            - add acceptance contraints
                - len, type
           
        - Create Selection Window(list names input, corresponding position output)     
            - file menus
            - typing drill functions ending in _exercise
            - boolean true false options
            
        - Create Static Window(Fitted_paragraphs, no output)
            - trigger response to end
            - can navigate pages
            
        - Create Type Text Window(Fitted_paragraphs, stats output)
            - sponge typer
            - typer
            - can navigate pages
        
    - #utilities.py      
        - get text
            - get url
            - get clipboard
            - from file
        - process text
            - fit text to screen
                - fit to width
                - fit to hight

        - analyze typed text
            - return typing analytics