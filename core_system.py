from register import RegisterController
from login import Login
from fundingSystem import FundingSystem



print('welcome to the CROWDFUNCDING system')

while True:
    choice = input('Sign up or Log in : ')
    if choice == 's':
        RegisterController()
    elif choice == 'l':
        person = Login()
        if isinstance(person.list,list) :
            
            system = FundingSystem(person.list)
        else:
            print('this data is not in our database')    

    elif choice == 'quit':
        print('bye')
        break    



