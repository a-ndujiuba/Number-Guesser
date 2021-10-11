LOW = 1
HIGH = 1000

start = input("Press ENTER to Start")
print(f"Think of a number between {LOW} and {HIGH}")
next_step = input("Press ENTER when you have thought of a number")


def guess_binary(low, high):
    guesses = 1
    while True:
        guess = low + (high - low) // 2
        print(f"Is {guess} the number you were thinking of?")
        high_low = input('Type "l" to guess lower, "h" to guess higher, and "c" if I was correct ')

        if high_low == 'h':
            low = guess + 1
            guesses += 1
        elif high_low == 'l':
            high = guess - 1
            guesses += 1
        elif high_low == 'c':
            print("I got it in {} guesses!".format(guesses))
            break

    return guesses


guess_binary(LOW, HIGH)
