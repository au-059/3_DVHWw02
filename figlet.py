import sys
import random
from pyfiglet import Figlet

figlet = Figlet()
text = input("Text: ")

# If the user inputs zero arguments, output in RANDOM FONT
if len(sys.argv) == 1:
    random_f = random.choice(figlet.getFonts())
    figlet.setFont(font=random_f)
elif len(sys.argv) == 3 and (sys.argv[1] == "-f" or sys.argv[1] == "--font"):
    try:
        figlet.setFont(font=sys.argv[2])
    except:
        sys.exit("Invalid usage")
else:
    sys.exit("Invalid usage")

print(figlet.renderText(text))