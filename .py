print("============expense tracker=============")
expense = []

def choice(): 
  while True:
    choice = int(input("enter your choice:"))
    if choice == 1:
      print("Add an expense")
      name = input("Enter expense name:")
      amount= float(input("Enter amount:"))
      category = input("Enter category:")
      
      dict = {'name': f"{name}", 
      'amount': f"{amount}",
      'category': f"{category}"}
      expense.append(dict)
      print("-------Expense Added Successfully-------")
    elif choice == 2:
      print("-------------View an expense------------")
      if not expense:
        print("no expense stored")
      else :
        for dict in expense:
           print(dict)
      
      
    elif choice ==3 :
      print("--------------View total expense--------------")
      sum = 0
      for dict in expense:
        sum += float(dict['amount'])
      print(f"Total Expense: {sum}")
        
        
    elif choice == 4:
      print("-----------------Search by category--------------")
      search = input("enter the category: ")
      found = False 
      for dict in expense:
          if dict['category'].lower() == search.lower():
                print(f"{dict['name']}")
                print(f"{dict['amount']}")
                found = True
      if not found:
            print("category not found")
    elif choice == 5:
      print("----------------exit------------------")
      break

choice()