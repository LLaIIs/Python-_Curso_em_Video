#Cores no terminal
#ANSI(escape sequence)
#\033[style;text;background m
"""Style            text          "   "   background
     0 none          30 black     "   "   40
     1 bold          31 red       "   "   41
     4 underline     32 green     "   "   42
     7 negative      33 yellow    "   "   43
                     34 blue      "   "   44
                     35 Magenta   "   "   45
                     36 cyan      "   "   46
                     37 grey      "   "   47
                     97 white     "   "   107"""
print('\033[0;30;41m Olá mundo!\033[m')
print('\033[4;33;44 m Olá mundo!\033[m')
print('\033[1;35;43 m  Olá mundo!\033[m')
print('\033[30;42m Olá mundo!\033[m')
print('\033[m Olá mundo!\033[m')
print('\033[7;97m Olá mundo!\033[m')
print('\033[4;97;45m Olá mundo\033[m')




