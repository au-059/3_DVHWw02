import emoji
import sys

if len(sys.argv) == 2:
    emojized = emoji.emojize(sys.argv[1])
    print(emojized)

# INPUT ---> :thumbs_up: