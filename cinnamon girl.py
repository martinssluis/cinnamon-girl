import sys
from time import sleep
import time 

def print_lyrics():
    lines = [
        ("There's things I wanna say to you", 0.04),
        ("But I'll just let you live", 0.05),
        ("Like if you hold me without hurting me", 0.06),
        ("You'll be the first who ever did", 0.1),
        ("There's things I wanna talk about", 0.08),
        ("But better not to give", 0.1),
        ("But if you hold me without hurting me", 0.07),
        ("You'll be the first who ever did", 0.05)
    ]

    delays = [0.3, 0.3, 0.3, 0.3, 0.4, 0.3, 0.1, 0.6, 0.07, 0.3, 0.5]

    for i, (line, char_delay) in enumerate(lines):
        for char in line:
            print(char, end='')
            sys.stdout.flush()
            sleep(char_delay)
        time.sleep(delays[i])
        print('')

print_lyrics()
