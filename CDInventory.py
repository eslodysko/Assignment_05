#------------------------------------------#
# Title: CDInventory.py
# Desc:  Script for Adding, Displaying, Saving and Loading CD Inventory
# Change Log: (Who, When, What)
# DBiesinger, 2030-Jan-01, Created File
# Eslodysko, 2022-Nov-12, Modofied File
#------------------------------------------#

# Declare variabls
strChoice = '' # User input
lstTbl = []  # list of lists to hold data
lstRow = []  # list of data row
dicRow = {}
strFileName = 'CDInventory.txt'  # data storage file
objFile = None  # file object

# Get user Input
print('The Magic CD Inventory\n')
while True:
# 1. Display menu allowing the user to choose:
    print('[a] Add CD\n[i] Display Current Inventory\n[l] load Inventory from file')
    print('[d] delete CD from Inventory\n[s] Save Inventory to file\n[x] exit')
    strChoice = input('l, a, i, d, s or x: ').lower()  # convert choice to lower case at time of input
    print()
        
# 2. Add data to the table (2d-list) each time the user wants to add data
    if strChoice == 'a':  # ADD DICTIONARIES TO LIST
        strID = input('Enter an ID: ')
        strTitle = input('Enter the CD\'s Title: ')
        strArtist = input('Enter the Artist\'s Name: ')
        intID = int(strID)
        dicRow = {'ID': intID, 'Title': strTitle, 'Artist': strArtist} #creates dictionary row
        lstTbl.append(dicRow) #APPENDS dictionary to 2-D List
        
# 3. Display the current data to the user each time the user wants to display the data
    elif strChoice == 'i': #DISPLAY CURRENT LIST OF DICTIONARIES
        print('ID, CD Title, Artist')
        for row in lstTbl:
            print(*row.values(), sep = ', ')
            
    elif strChoice == 'l': #LOAD INVENTORY FROM FILE
        # TODO Add the functionality of loading existing data
        lstTbl.clear() #CLEAR LSTTBL OF OLD DICTIONARY LISTS
        objFile = open(strFileName, 'r') #OPEN and READ FILE
        for row in objFile:
            lstRow = row.strip().split(',') #REMOVES TEXTFILE STRING FORMATTING
            dicRow = {'ID': lstRow[0], 'Title': lstRow[1],'Artist': lstRow[2]} #EACH PAIRING INTO DICROW
            lstTbl.append(dicRow)
        objFile.close
    
    elif strChoice == 'd': #DELETE ENTRY SPECIFIED BY USER
         delId = input("Enter CD ID to delete: ")
         for row in lstTbl: # OPEN EACH DICT IN LIST
             if delId in row:
                 del lstTbl[delId]
             print('\nDeleted', delId, '\n')
         else:
            print("\nDelete not complete", delId, "doesn't exist in inventory.")
          
# 4. Save the data to a text file CDInventory.txt if the user chooses so          
    elif strChoice == 's': # SAVE TO FILE
        objFile = open(strFileName, 'a')
        for row in lstTbl:
            strRow = ''
            for item in row.values():
                strRow += str(item) + ','
            strRow = strRow[:-1] + '\n'
            objFile.write(strRow)
        objFile.close()

# 5. Exit the program if the user chooses so
    elif strChoice == 'x': #EXIT THE PROGRAM
        break
    else:
        print('Please choose either l, a, i, d, s or x!')
        
        
        
# DELETE ENTRY OPTIONS:

    # delID = input('Enter ID to Remove from Inventory: ')
       # delIDInt = int(delID)
       # for row in lstTbl:
           # for cell in row:
               # if delIDInt in cell:
                    #lstTbl.remove(row)
            #else:
               # print(delID, 'Not sucessful')
     
        # ATTEMPT  2
        #userD = input('Enter CD ID to Delete: ')
        # userIntD = int(userD)
        # for row in lstTbl:
            # if lstTbl[intID] == userIntD:
                # row.clear()
         
       # ATTEMPT  3
        #term = input("What term do you want me to delete?: ")
        #for dicRow in lstTbl: # OPEN EACH DICT IN LIST
          #   if term in dicRow:
               #  del lstTbl[term]
            # print('\n Deleted', term, '\n')
         #else:
           #  print("\nI can't complete", term, "doesn't exist.")
           #  print()
           #  print(lstTbl)
           #  print()