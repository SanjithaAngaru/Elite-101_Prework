print("Welcome to ChatbotA01! I'll be here to help you today!")
#name and age variables
name = input("What's your name? :")
age = input(f"Awesome {name}! How old are you!? :")
#intro statement + name and age variables
print(f"Wow {name}! I can't belive your already {age}! Time flies by fast, don't you think?!")
print(f"Well, moving on {name}! I am here to help you for any means neccessary for any questions about this tutoring program!")
#asking user how it can help them 
user_select = input("What would you like to know about this tutoring program? \n*press 1 for about\n*press 2 for course options\n*press 3 for contact information \n*press 4 to leave ChatbotA01 \n Enter your answer here: ")
if user_select =="4":
        #exit statement
        print(f"Goodbye {name}! See you next time :)")
        print("Shutting down...")
        exit()
elif user_select != 4:
  while user_select != 4:    
      if user_select == "1":
          pass 
      elif user_select =="2":
          pass 
      elif user_select =="3":
          pass 
      else:
          print(f"Didn't get it? That's ok {name}!")
          pass
