import sys
import time
print("Welcome to ChatbotA01 Food Delivery! I'll be here to help you today!")

#name and age variables
name = input("What's your name? :")
age = input(f"Awesome {name}! How old are you!? :")


#receipt number variables
receipt_number = len(name)
#intro statement + name and age variables
print(f"Wow {name}! I can't belive your already {age}! Time flies by fast, don't you think?!")
print(f"Your receipt number is {receipt_number} ")
print(f"Well, moving on {name}! I am here to help you for any means neccessary for any questions about your food delivery services and questions you need to ask!")
time.sleep(2)

#when the user chooses option 2.
def option_two():
    location = input("You have pressed option 2. \nPlease enter your your location: ")
    receipt_number = input("Please re-enter your receipt number:")
    if receipt_number != len(name): 
        print("Invalid reciept number")
    elif receipt_number == len(name):
        print(f"Nice {name} - we are contacting your driver about your food delivery!. ")
        print("Processing...")
        time.sleep(1)
        print("Great! You can contact your driver for more information!")
        option_three()

    


def option_three():
    list = ['Chickfila', 'Burger King', 'Dominoes','Panda Express']
    print("You have pressed option 3.")
    option_three_input = input("Where did you order your food from: ")
    if list != option_three_input:
        print("Invalid option. We do not have connections to that food chain.")
    elif list == option_three_input:
        print("Processing...")
        time.sleep(1)
        if option_three_input == 'Chickfila':
            print("Your driver's contact number is ----> (233-356-7900)")
            print("If you cannot contact your driver's number at this time, here is the managers number: (384-654,3455)")
        elif option_three_input == 'Burger King':
            print("Your driver's contact number is ----> (123-456-7890) (DISCLAIMER: Do NOT Call this number - these are fake.)")
            print("If you cannot contact your driver's number at this time, here is the managers number: (384-654,3455)")
        elif option_three_input == 'Dominoes':
            print("Your driver's contact number is ----> (113-436-7891)")
            print("If you cannot contact your driver's number at this time, here is the managers number: (384-654,3455)")
        elif option_three_input == 'Panda Express':
            print("Your driver's contact number is ----> (323-459-7000)")
            print("If you cannot contact your driver's number at this time, here is the managers number: (384-654,3455)")
    time.sleep(0.5)
    print(f"Thank you for using ChatbotA01 Food Delivery. See you next time {name}!")
    sys.exit()
    

    def option_one():
        time.sleep(0.5)
        print(f"Okay {name}, I see you're interested about our services!")

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
        option_three()
        True
    elif user_select == "4":
        print(f"Shutting down, thank you for your time today {name}")
        sys.exit()
        False
    else:
        print("Invalid Option, please pick from the 1-4")

