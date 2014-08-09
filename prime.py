'''
Created on 2014.08.09.

@author: David
'''
import sys
    
def is_prime(input):
    status = True
    if input < 2:
        status = False
    else:
        for i in range(2,input):
            if input % i == 0:
                    status = False
        return status
    
def prime_numbers_below_n(input):
    
    prime_list = []
    
    if is_prime(input) == True:
        print 'ez egy kibaszott prim'
        prime_list.append(input)
    else:
        for n in range(1,(input/2)+1):
                        
            if (is_prime(n)== True):
                prime_list.append(n)
                
    return prime_list

def is_prime_divider(input):
    dividers = []
    
    numbers = prime_numbers_below_n(input)
    for n in numbers:
       
        if input % n == 0:
            dividers.append(n)
    
    return dividers


def prime_factors(input):
    
    divs = is_prime_divider(input)
    szar = [] 
    for number in divs:
        while((input % number) == 0):
                      
            print 'pina'
            szar.append(number)
            input = input/number
            #print str(input) +'osztva '  + str(number) + '-vel/val az : ' + str(input / number)
    
    return szar

def main(argv):
    
    x = input("Enter a number:")
    print "input =", x
    
    print is_prime_divider(x)
    print 'primtenyezos felbontas' + str(prime_factors(x))
      
if __name__ == "__main__":
        main(sys.argv[1:])
