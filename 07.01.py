from calendar import month
month=int(input("Enter month number:"))
match month: 
     case month if month in (1,3,5,7,8,10,10):
         print("31 days")
     case month if month in (2,4,6,9,11):
         print("30 days")   
     case 2:
         print("28 or 29 days")
     case _:
         print("Invalid month number:")   
print()           
