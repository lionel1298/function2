#given year of birth  provided by user calculate and age of user 
#use atleast one function 
#prompt the user for date of birth 
#one of your function should have one or more parameters 


def get_age(year_of_birth,current_year):
    age=0
    age=current_year-year_of_birth
    return age
    
   
def user_input():
    yob= int(input("enter your year of birth"))
    currentYear=int(input("enter current year" ))
    age1 =get_age(yob,currentYear)
    print (age1)

user_input()
