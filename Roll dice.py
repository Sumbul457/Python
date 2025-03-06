from random import randint

result = 0
n = 1

while n <= 3:
    print("\nWelcome to dice roll 🎲")
    input("Press Enter to roll...")

    you = randint(1, 6)
    result += you
    print(f"\nYou rolled: {you}")

    # Dice Face Representation
    dice_faces = {
        1: "🎲\n.  \n   \n   \n",
        2: "🎲\n.  \n   \n  .\n",
        3: "🎲\n.  \n . \n  .\n",
        4: "🎲\n. .\n   \n. .\n",
        5: "🎲\n. .\n . \n. .\n",
        6: "🎲\n. .\n. .\n. .\n"
    }

    print(dice_faces[you])

    n += 1  # Increase the roll count

print(f"\nThe total result of your three rolls is {result} 🎲")










    