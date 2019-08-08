f = open("Data.txt", "r")
word = f.read().lower()
f.close()
show = "_" * len(word)

print(show)

list1 = list(show)
alive = True
correct = False
lives = 10
letters_left = len(word)

while alive:
    quess = str(input("Enter a letter:"))
    if quess == "quit":
        break
    if len(quess) > 1:
        print("\"Enter just ONE letter")
        continue

    for i in range(len(word)):
        if quess.lower() == word[i]:
            list1[i] = quess
            letters_left -= 1
            correct = True
        if letters_left == 0:
            break

    if not correct:
        lives -= 1
        print("\nWrong letter")
        print("Left: " + str(lives) + " lives")
    if lives == 0:
        alive = False
    show = ''.join(list1)
    print("\n" + show)

    if letters_left == 0:
        break
    correct = False


if lives > 0 and letters_left == 0:
    print("You Won:)")
elif lives == 0:
    print("You Lost:(")
elif lives > 0 and letters_left != 0:
    print("Game Canceled")
