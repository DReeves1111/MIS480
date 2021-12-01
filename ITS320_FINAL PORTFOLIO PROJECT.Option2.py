#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Program name: ITS 320 Final Portfolio Option 2
# Author: David Reeves
# Date: February 6, 2021
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Pseudocode:
# 1) Create a class called House_Inventory with different attributes that are private
# 2) Create the program so that the user can add a new house to the inventory list
# 3) The user will enter the house's address, city, state, zipcode, sq. foot, sale status, and model
# 3) The program also allows the user to remove a house from the inventory list
# 4) The user can update a house in the inventory list, by entering a new address, city, state, zip, sq. ft, sale status, and model
# 5) The user can output the contents of the inventory list, by selecting what file name they want to save the info to
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Program Inputs: The user will add a house to the inventory list by entering the address, city, state, zip, sq. ft, sale status, and model
# Program Outputs: If the user wants to output the contents of the inventory list, they can enter whatever they want to name the file, and the file will be saved to their computer
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------



class House_Inventory:

    def __init__(self):
        self.address = ''
        self.city = ''
        self.state = ''
        self.zipcode = 0
        self.squarefeet = 0
        self.salestatus = ''
        self.modelname = ''
       

    def AddNewHouse (self):
        self.address = input('Please enter the street address of the house:')
        self.city = input('Please enter the city where the house is located:')
        self.state = input('Please enter the state where the house is located:')
        self.zipcode = input('Please enter the zip code where the house is located:')
        self.squarefeet = int(input('How many square feet is the house?'))
        self.salestatus = input('Please enter the sales status of the house (available, sold, under contract):')
        self.modelname = input('Please enter the model name of the house:')
        print('The house has been added to the inventory list') 

    def RemoveHouse (self):
        self.address = ''
        self.city = ''
        self.state = ''
        self.zipcode = 0
        self.squarefeet = 0
        self.salestatus = ''
        self.modelname = ''
        print('The house has been removed from the inventory list')

    def UpdateHouse (self):
        self.address = input('Please enter the updated street address of the house:')
        self.city = input('Please enter the updated city where the house is located:')
        self.state = input('Please enter the updated state where the house is located:')
        self.zipcode = int(input('Please enter the updated zip code where the house is located:'))
        self.squarefeet = int(input('Please enter the updated square footage of the house:'))
        self.salestatus = input('Please enter the updated sale status of the house (available, sold, under contract):')
        self.modelname = input('Please enter the updated model name of the house:')
        print('The attributes of the house have been updated')

    def GetAddress(self):
        return self.address

    def GetCity(self):
        return self.city

    def GetState(self):
        return self.state

    def GetZipcode(self):
        return self.zipcode

    def GetSquarefootage(self):
        return self.squarefeet

    def GetSalestatus(self):
        return self.salestatus

    def GetModelname(self):
        return self.modelname

house = []
while(True):
    print('1. Add house to inventory list')
    print('2. Remove house from inventory list')
    print('3. Update the attributes of a house')
    print('4. Save inventory to a file')
    print('5. End')
    response = int(input('Choose a command. 1-5: '))
    if(response == 1):
        Housecharacteristics = House_Inventory()
        Housecharacteristics.AddNewHouse()
        house.append(Housecharacteristics)
    elif(response == 2):
        address = input('Please enter the street address of the house that you want to remove: ')
        index = -1
        for i in range(len(house)):
            if(house[i].GetAddress() == address):
                index = i
                break
        if(index != -1):
            house[index].RemoveHouse()
            del house[index]
        else:
            print('Address provided is not listed in the inventory')
    elif(response == 3):
        address = input('Please enter the address you want to update: ')
        index = -1
        for i in range(len(house)):
            if(house[i].GetAddress() == address):
                index = i
                break
        if(index != -1):
            house[index].UpdateHouse()
        else:
            print('Address provided is not listed in the inventory')
    elif(response == 4):
        userinput = input('Please enter the name of the text file you would like to output all home inventory to:')
        outfile = open(userinput, 'w')
        for index in range(len(house)):
            outfile.write(str(index + 1)+'\n')
            outfile.write(house[index].GetAddress()+'\n')
            outfile.write(house[index].GetCity()+'\n')
            outfile.write(house[index].GetState()+'\n')
            outfile.write(str(house[index].GetZipcode())+'\n')
            outfile.write(str(house[index].GetSquarefootage())+'\n')
            outfile.write(house[index].GetSalestatus()+'\n')
            outfile.write(house[index].GetModelname()+'\n')
        outfile.close()
    elif(response == 5):
        break
    else:
        print('Error. Choose another response')
            


  
    

    
    
        

