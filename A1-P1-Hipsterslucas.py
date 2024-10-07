#Program 1 – Hipster's Local Vinyl Records
#Hipster’s Local Vinyl Records sell and hand-deliver vinyl records to their customers.

def main():
    # YOUR CODE STARTS HERE, each line must be indented (one tab)  
    #the code will first ask for all the user inputs 
    #then it will assign the value of each variable
    #it will then create new variables for the result of multiplying each other variables
    #then the those final variables will be printed out
    name=input("what is your name?")
    kilometer=float(input("how many kilometers is it"))
    sales=float(input("how many records are you buying?"))
    salestax=0.14
    delivery=15
    salescost=30
    deliverycost=delivery*kilometer
    recordscost=salescost* salestax/100
    totalcost=(salescost*salestax/100)*(delivery*kilometer)
    print(name)
    print(deliverycost)
    print(recordscost )
    print(totalcost )
    # YOUR CODE ENDS HERE
main()