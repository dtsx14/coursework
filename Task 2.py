#Task 2 Pseudocode - Checking and updating a stock file after an order
cont = ('y')
while cont == ('y'):
    print ('---------------------------------------------------')
    print ('  Welcome, please enter your GTIN-8 Product code')
    print ('---------------------------------------------------')
    #Records the users input into a variable called gtinCode
    gtinCode = input()
    print ('And how many of those would you like?')
    quantity = input()
    #Figures out the length of the string that the user has entered
    lenofstring = len(gtinCode)
    if lenofstring is not 8 :
        print ('Im sorry, the product code that you entered was not valid, please try again')
        cont = ('y')
    else:
        print("------Loading the stock file - this won't take a minute------")
        stockfile=open("//Client/N$/GCSE Computer Science/A453/Python/Stockfile.txt", "r") #this opens the text file
        stockline=stockfile.readlines() #reads the file and stores it as the variable 'stockfile' stockfile.close() closes the file)  
        for line in stockfile:
            if (gtinCode) in line: 
                print ("Here we go, I've found the product that you were looking for!")
                print line
                print ("Does that look okay?")
            else:
                print ("I'm sorry, the product that you were searching for could not be found. Press y to try again, or press q to quit"
                if input() == ('y'):
                    cont = ('y')
                else:
                    quit
else:
    print ('Thanks, we hope you are satisfied with your purchase')
    quit
