rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

import random 

choice = input("What do you choose? Type 0 for rock, 1 for paper, or 2 for scissors. \n" )

if choice == 0:
    print(f"You chose rock {rock}.")
elif choice == 1:
    print(f"You chose paper {paper}.")
else:
    print(f"You chose scissors {scissors}.")

computer_selection = random.randint(0,2)

if computer_selection == 0:
    print(f"Computer chose {rock}.")
elif computer_selection == 1:
    print(f"Computer chose {paper}.")
else:
    print(f"Computer chose {scissors}.")
    
# if choice == 0 and computer_selection == 0:
#     print("Draw.")
# elif choice == 0 and computer_selection == 1:
#     print("You lose.")
# elif choice ==0 and computer_selection == 2:
#     print("You win.")

# if choice == 1 and computer_selection == 0:
#     print("You win.")
# elif choice == 1 and computer_selection == 1:
#     print("Draw.")
# elif choice ==1 and computer_selection == 2:
#     print("You lose.")

# if choice == 2 and computer_selection == 0:
#     print("You lose.")
# elif choice == 2 and computer_selection == 1:
#     print("You win.")
# elif choice ==2 and computer_selection == 2:
#     print("Draw.")
