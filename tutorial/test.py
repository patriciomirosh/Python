import traceback
from myloggers import mylogger 
logger=mylogger()

class testfunction:
       
    logger.debug('The program is function well')
    print("====================================")
    print(" ")
    print("Introduce any ID, the program will be generated a password for you this time ")
    print("")
    Users = input("User ID: ")
    print("====================================")
    print("")
    print("Your passwordtest is ({}{}) try with that ".format(Users[-1:0:-1], Users[0]))
    print("")
    print("====================================")
    password = input("Introduce your password :")
    testpasword = "{}{}".format(Users[-1:0:-1], Users[0])
    if password != testpasword:
        logger.critical("The password is incorrect, you not have access to the program, the program will be closed")
        exit()
    logger.info("everything is fine")
    def __init__(self, x, y):
        try:
            self.result=x/y

        except :
            logger.error("The log of the error are %s", traceback.format_exc())
        
    def adde(self,x,y):
        try:
            adde=x+y
        except:
            logger.error("The program cant add this values")
        try:
            return adde,  logger.info('The program is okay and the result are {}'.format(adde))
        except:
            logger.error("The variables input cannot be added")
    def doingyouremail(self):
        name=input("Introduce your name, and last name separed by a space: ")
        FirstName=name.split(" ")[0]
        try:
            LastName=name.split(" ")[1]
        except:
            logger.critical("The user didn't introduce at least 2 words, the program cannot will be doing his email")
        try:    
            if len(FirstName)+len(LastName)>=20:
                logger.warning("The name is too large your email will be difficult to memorize")
            email="{}.{}@mycompany.com".format(FirstName, LastName)
            logger.info("dear user your credencials are/ name: {}, last: {}, email:  {} /".format(FirstName, LastName,email))
        except: 
            logger.info("Please introduce your first name and last name")
        
        
pato1=testfunction(2, 0)
pato1.adde("a",1)
pato1.doingyouremail()

