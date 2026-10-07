import random

computer = random.choice([-1, 0, 1])
you_dict = {"s": 1, "w": -1, "g": 0}
reverse_dict = {1: "Snake", -1: "Water", 0: "Gun"}
choice = input("Enter your choice (s/w/g): ").strip().lower()
you = you_dict.get(choice)

if you is None:
    print("Invalid choice! Please enter s, w, or g.")
else:
    print(f"You choose {reverse_dict[you]} and computer choose {reverse_dict[computer]}")

    if computer == you:
        print("Match Draw!")
    elif (computer == 1 and you == -1) or \
            (computer == -1 and you == 0) or \
            (computer == 0 and you == 1):
        print("You Lose!")
    else:
        print("You Win!")