#Program to calculate and check GTIN product codes
cont=('y')
count=0
#These two lines define the variables to begin with
total=0
#This line asks the user to input their product code and automatically deduces whether they want to check a product code or calculate one
while cont == ("y"):
    count=0
    total=0
    print ('-------------------------------------------------')
    print (' Welcome, please enter a 7 or 8 digit GTIN code')
    print ('-------------------------------------------------')
    #Records the users input into a variable called gtinCode
    gtinCode = input()
    #Figures out the length of the string that the user has entered
    lenofstring = len(gtinCode)
    #Starts the process of calculating the code if the user has entered 7 digits
    if (lenofstring) == 7 :
        #Changes the integer into a string so that it can be processed
        number_string = str(gtinCode)
        #Separates the code into individual digits for calculation
        for ch in number_string:
            #Changes the individual charactor back into an integer 
            ch = int(ch)
            #This whole statement figures out if the number is odd or even
            if (count % 2 == 0): #Even
                #Multiplys the number by 3
                numcalc = ((ch) * 3)
                #Adds the result to the total
                total = (total)+(numcalc)
                #Adds the count + 1 to tell which number is odd or even
                count = (count) + 1
            else: #Odd
                #Puts the number into a variable to be added on
                numcalc = (ch)
                #Total as before
                total = (total)+(numcalc)
                #As above
                count = (count) + 1
        #Figures out what number is the nearest 10 and processes this 
        nearest10 =((total) % 10)#Needs fixing to round up
        #Changes the GTIN code back into a string to be outputted as print 
        gtinCode = str(gtinCode)
        #As above but for the nearest10 variable
        nearest10 = str(nearest10)
        #Outputs the end result of the code
        print(('Your finished GTIN-8 code with check digit is: ') + (gtinCode)+(nearest10))
        print ('Would you like to do another code? (Y/N)')
        cont = input()
    #Selects the option for if the user wants to validate a code
    elif (lenofstring) == 8:
        #For this section of code see above
        number_string = str(gtinCode)
        for ch in number_string:
            #Changes the individual charactor back into an integer 
            ch = int(ch)
            #This whole statement figures out if the number is odd or even
            if (count % 2 == 0): #Even
                #Multiplys the number by 3
                numcalc = ((ch) * 3)
                #Adds the result to the total
                total = (total)+(numcalc)
                #Adds the count + 1 to tell which number is odd or even
                count = (count) + 1
            else: #Odd
                #Puts the number into a variable to be added on
                numcalc = (ch)
                #Total as before
                total = (total)+(numcalc)
                #As above
                count = (count) + 1
        #Figures out what number is the nearest 10 and processes this 
        nearest10 =((total) % 10)#Needs fixing to round up
        #Changes the GTIN code back into a string to be outputted as print 
        gtinCode = str(gtinCode)
        #As above but for the nearest10 variable
        nearest10 = str(nearest10)
        #Checks the check digit against the rest of the code
        finishedCode = (gtinCode [:-1]) + (nearest10)
        if (finishedCode) == (gtinCode):
            print ('Your code is valid')
        else:
            print ('Your code is invalid')
        print ('Would you like to do another code? (Y/N)')
        cont = input()
        #Selects the option if the user has entered an invalid code
    else:
        print ("I'm sorry, the code that you entered was not 7 or 8 digits, would you like to try again?(Y/N)")
        cont = input()
else:
    quit()
