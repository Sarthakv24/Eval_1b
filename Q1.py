<DOCTYPE!>
def display_menu():
    print('\n ADVANCED CONTACT MANAGEMENT SYSTEM')
    print('\n MAIN MENU')
    print('1. Add Contacts')
    print('2. Update Contacts')
    print('3. Delete Contacts')
    print('4. List All Contacts')
    print('5. Searching Contacts')
    print('6. Listing Contacts By Initial Names')
    print('7. Go Back')
    print('8. Exit')

def Add_Contacts(Contacts):
    New_Contact_Name= input('Enter New Contact Name:)
    Phone_number= input('Enter the ')                        
                            
def main():
    display_menu()
    choice = input ('Choose An Option: ')
    if  choice=='1':
        Add_Contacts(Contacts)
    else  choice=='2':
        Update_Contacts(Contacts)
    else  choice=='3':
        Delete_Contacts(Contacts)
     else  choice=='4':
        List_All_Contacts(Contacts)
    else  choice=='5':
        Searching_Contacts(Contacts)
     else  choice=='6':
        Update_Contacts(Contacts)
    else  choice=='7':
        Add_Contacts(Contacts)
    else  choice=='8':
        exit
        
