import random
import string
from random import*

alfabe=string.ascii_letters
numeriq=string.digits
alfabenumeriq=alfabe+numeriq

#1
def invesmo(mo):
    print(mo[::-1])


#2
def kodalealeyatwa():
    # alfabe=string.asci_letters
    nkarackte=randint(1,61)
    kod=""
    for i in range (nkarackte):
        index=randint (0,25)
        kod+=alfabe[index]
        print(kod)

        #3
def kodaleatwa():
    nkarakte=randint(2,61) 
    kod=""
    for i in range(nkarakte):
     index=randint(0,25)   
    if alfabe[index] in kod:
         index=randint(0,25)
        
    else:
             kod+=alfabe[index]
    print(kod)
   
   #4
    def  alfabenumeriq():
         nkarakte=randint(2,61)
         kod=""
         for i in range[nkarakte] in kod:
          nkarakte=randint(2,61)
         else:
         
          kod+=alfabenumeriq[nkarakte]
           
    print(kod)  

    #5
    def functionslug():    
        chenn=input("antre frazz  :;\n") 
        chenn=chenn.lower()
        lotchenn=""
        slug=""
        for i in chenn:
            if i== " ";
                lotchenn=chenn.replace(" ", "-")
        for i in chenn:
            if i==" ":
                lotchenn=chenn.replace(" ", "-")
                for i in lotchenn:
                    slug+=i
                    print(slug)
                    #6 
                def separeakvigil():
                    mo=input ("mete mo an ::")
                    nouvomo=""
                    for i in mo:
                        nouvomo+=i+","
                  print(nouvomo)
                    
                


