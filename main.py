print("Welcome to ChatbotA01 Food Delivery! I'll be here to help you today!")

#name and age variables
name = input("What's your name? :")
age = input(f"Awesome {name}! How old are you!? :")


#receipt number variables
for i in name:
    name+=1

#intro statement + name and age variables
print(f"Wow {name}! I can't belive your already {age}! Time flies by fast, don't you think?!")
print("Your receipt number is ____")
print(f"Well, moving on {name}! I am here to help you for any means neccessary for any questions about your food delivery services and questions you need to ask!")

while True:
    #asking user how it can help them 
    user_select = input("What would you like to know about this food delivery \n*press 1 for about\n*press 2 for questions \n*press 3 for the driver information contact \n*press 4 to leave ChatbotA01 \n Enter your answer here: ")
    if user_select == "1":
        print("Hello, it seems like you have pressed 1. ")
        True
    elif user_select == "2":
        option_two()
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
def option_two():
    location = input("You have pressed option 2. \nPlease enter your your location: ")
    receipt_number = input("Please re-enter your receipt number:")
    if receipt_number not in 
    
    
    
