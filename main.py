<<<<<<< HEAD
import time
=======

print("Welcome to ChatbotA01 Food Delivery! I'll be here to help you today!")

#name and age variables
name = input("What's your name? :")
age = input(f"Awesome {name}! How old are you!? :")
receipt number = 0 

#receipt number variables
for add in name:
    receipt number+=1


#receipt number variables
receipt_number = len(name)
#intro statement + name and age variables
print(f"Wow {name}! I can't belive your already {age}! Time flies by fast, don't you think?!")
<<<<<<< HEAD
print(f"Your receipt number is {receipt_number} ")
print(f"Well, moving on {name}! I am here to help you for any means neccessary for any questions about your food delivery services and questions you need to ask!")

time.sleep(2)


#when the user chooses option three 
def option_three():
    list = ['Chickfila', 'Burger King', 'Dominoes','Panda Express']
    
    while True:
        option_three_input = input("Where did you order your food from? : ").title()
        if option_three_input not in list:
            print("Invalid option. We do not have connections to that food chain.")
        elif option_three_input == 'Chickfila' or 'Chick-fil-a':
            print("Processing...")
            print(f"Awesome {name}! Here is your driver and manager's information!")
            time.sleep(1)
            print("Your driver's contact number is ----> (233-356-7900)")
            print("If you cannot contact your driver's number at this time, here is the managers number: (384-654,3455)")
            break
        elif option_three_input == 'Burger King':
            print("Processing...")
            print(f"Awesome {name}! Here is your driver and manager's information!")
            time.sleep(1)
            print("Your driver's contact number is ----> (123-456-7890) (DISCLAIMER: Do NOT Call this number - these are fake.)")
            print("If you cannot contact your driver's number at this time, here is the managers number: (384-654,3455)")
            break
        elif option_three_input == 'Dominoes':
            print("Processing...")
            print(f"Awesome {name}! Here is your driver and manager's information!")
            time.sleep(1)
            print("Your driver's contact number is ----> (113-436-7891)")
            print("If you cannot contact your driver's number at this time, here is the managers number: (384-654,3455)")
            break
        elif option_three_input == 'Panda Express':
            print("Processing...")
            print(f"Awesome {name}! Here is your driver and manager's information!")
            time.sleep(1)
            print("Your driver's contact number is ----> (323-459-7000)")
            print("If you cannot contact your driver's number at this time, here is the managers number: (384-654,3455)")
            break
        time.sleep(0.5)

#when the user chooses option 2.
def option_two():
    while True:
        receipt_number = input("Please re-enter your receipt number:")
        if int(receipt_number) != len(name):
            False
            print("Invalid receipt number")
        elif int(receipt_number) == len(name):
            print(f"Nice {name} - we are contacting your driver about your food delivery!")
            print("Processing...")
            time.sleep(1)
            print("Great! You can contact your driver for more information!")
            break
            

            
    
#when the user chooses option 1
def option_one():
    print(f"Nice {name}!")
    print("This chatbot is used to help your needs when you are in a hurry!")
    print(f"Need quick contact information or want to confirm that your receipt number is valid for refunds? We got you {name}! We are here to assist you, and that's our full job.")
    print("")


#introductory statements
while True:
    #asking user how it can help them 
    print("      ")
    user_select = input("What would you like to know about this food delivery? \n*press 1 for about\n*press 2 for reciept number comformation \n*press 3 for driver information contact \n*press 4 to leave ChatbotA01 \n Enter your answer here: ")
    if user_select == "1":
        option_one()
=======
print("Your receipt number is ____")
print(f"Well, moving on {name}! I am here to help you for any means neccessary for any questions about your food delivery services and questions you need to ask!")

#defining functions
def option_two():
    location = input("You have pressed option 2. \nPlease enter your your location: ")
    receipt_number = input("Please re-enter your receipt number:")
    while True:   
        i = 3
        if receipt_number != reciept_number:
            False
            i -= 1
            print(f"Invalid Receipt number. You have {i} more attempts")
            if i = 0:
                print("Invalid Receipt number.Please try again next time.")
                exit()
            
        elif receipt_number = receipt_number:
            True
            print("Correct!")
            print(f"Great, now please check your email to see your order. Thank you for your patience {name}. See you next time")
            exit()
#user input
while True:
    #asking user how it can help them 
    user_select = input("What would you like to know about this food delivery \n*press 1 for about\n*press 2 for questions \n*press 3 for the driver information contact \n*press 4 to leave ChatbotA01 \n Enter your answer here: ")
    if user_select == "1":
        print("Hello, it seems like you have pressed 1. ")
        print("This chatbot is here to help you with whatever 
>>>>>>> 44238217995a268cf12d987dde6052888a671926
        True
    elif user_select == "2":
        option_two()
        True
    elif user_select == "3":
        option_three()
        True
    elif user_select == "4":
        print(f"Shutting down, thank you for your time today {name}")
        False
        #choosing option 4 ends the program
        break
    else:
        print("Invalid Option, please pick from the 1-4")
<<<<<<< HEAD
        True

=======

    
    
    
>>>>>>> 44238217995a268cf12d987dde6052888a671926
