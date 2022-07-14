# This is a basic choose your own adventure game
# This utilizes if, elif, and else statements
# ASCII art from https://ascii.co.uk/art/pawprints

print('''
   h  h
 h(")(")h
("),--.(")
 :"    ";
 `.____,' sk
 ''')
print("Welcome to the cat cafe!")
print("You need to find Garfield.")

choice1 = input('You walk into the cafe and meet a charming tom cat named Behemoth? Do you speak to him? Type "Yes" or "No".')

if choice1 == ('Yes').lower():
    choice2 = input('Behemoth is the barista standing on his hind legs as large as a boar. He asks, Would you like warm apricot soda? Type "Yes" or "No".')
    if choice2 == ('Yes').lower():
        choice3 = input('Behemoth invites you to a party. Do you say "Yes" or "No"?')
        if choice3 == ('Yes').lower():
            choice4 = input('You walk into the party and smell the scent of lasagna. Do you walk toward the italian goodness? Type "Yes" or "No".')
            if choice4 == ('Yes').lower():
                print('You walk over and see Garfield chatting with Behemoth. They are drinking apricot soda and having a great time. You found him! You Win!')
        else:
            print("You get kicked out for being rude to Behemoth!")
    else:
        print("Your head was cut off!")
else:
    print("The cat cafe diappears, and you are magically home in your bed.")
