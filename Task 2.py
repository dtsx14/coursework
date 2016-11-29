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
        for line in stockline:
            if (gtinCode) in line:
                splitfile = stockline.split
                #The stockfile is now split into a list to be able to see the quantity, the quantity is a single digit at the end of the list, so the program will always select that digit, and then check it against the quantity that is entered by the user
                itemquantity = splitfile[-1]
                if itemquantity < quantity:
                    print ("I'm sorry, there are not enough products available to fulfil your order, we only have " + itemquantity + (" left, press y to order another product, or press q to quit")
                    reorderfile = open("
                else:
                    print ("Here we go, I've found the product that you were looking for!")
                    print line
                
                
            else:
                print ("I'm sorry, the product that you were searching for could not be found. Press y to try again, or press q to quit")
                if input() == ('y'):
                    cont = ('y')
                else:
                    quit
else:
    print ('Thanks, we hope you are satisfied with your purchase')
    quit
