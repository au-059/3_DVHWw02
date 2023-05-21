import random

# Input level n (i.e. the maximum)
while True:
    try:
        level = int(input("Input: "))

        if level > 0:
            break
    except ValueError:
            pass

random_int = random.randint(1, level)

while True:
        try:
            guess = int(input("Guess: "))
            if guess > 0 and guess <= level:
                if guess < random_int:
                    print("Too small!")
                elif guess > random_int:
                    print("Too large!")
                else:
                    print("Just right!")
                    break
        except:
             pass