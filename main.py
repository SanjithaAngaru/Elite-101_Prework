print("Welcome to ChatbotA01 Food Delivery! I'll be here to help you today!")

#name and age variables
name = input("What's your name? :")
age = input(f"Awesome {name}! How old are you!? :")

#intro statement + name and age variables
print(f"Wow {name}! I can't belive your already {age}! Time flies by fast, don't you think?!")
print(f"Well, moving on {name}! I am here to help you for any means neccessary for any questions about this tutoring program!")

while True:
    #asking user how it can help them 
    user_select = input("What would you like to know about this tutoring program? \n*press 1 for about\n*press 2 for course options\n*press 3 for contact information \n*press 4 to leave ChatbotA01 \n Enter your answer here: ")
    if user_select == "1":
        print("This tutoring program is about...")
        True
    elif user_select == "2":
        print("Courses that the academy provides id...")
        True
    elif user_select == "3":
        print("More information")
        True
    elif user_select == "4":
        print(f"Shutting down, thank you for your time today {name}")
        exit()
        False
    else:
        print("Invalid Option, please pick from the 1-4")
