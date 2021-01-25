# game number is hide_number // we need to Match this number
hide_number = int(input("Give the game number : "))
# trying time to Match the number with hide_number
try_time = int(input("Trying time to guess : "))
# guess_hid use to run while loop
guess_hid = 0
# here e make the loop // if guess_hid time is small then try_time the the loop can work
while guess_hid < try_time:
    # here we are receiving our guess number
    guess = int(input("guess the number : "))
    # increasing the loop
    guess_hid += 1
    # matching the guess number with hide_number
    if guess == hide_number:
        print("You win")
        break
# other condition
else:
    print("You failed")
