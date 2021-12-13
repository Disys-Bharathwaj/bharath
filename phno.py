class phone_Contacts:                                                                                   #OOPS
    
    def __init__(self,Firstname,Lastname,Phone_number,Email_ID,Groups,DOB):                             #function
        self.firstname=Firstname
        self.lastname=Lastname
        self.phonenumber=Phone_number
        self.emailid=Email_ID
        self.groups=Groups
        self.dob=DOB
        
        
    def open_phcontacts(self):
        print("Phone Contacts")
    
        
    def firstname_verification(self):
        if type(self.firstname) == str:
            if len(self.firstname) <= 15:                                                                                #LEN FUNCTION
                print("Firstnameame verified")
            else:
                raise ValueError("Firstnameame should contain lesser than or equal to 15 letters")
        else:
            raise TypeError("Firstname should contain letters only")
        
    def lastname_verification(self):
        if type(self.lastname) == str:
            if len(self.lastname) <= 15:                                                                                #LEN FUNCTION
                print("Lastnameame verified")
            else:
                raise ValueError("Lastnameame should contain lesser than or equal to 15 letters")
        else:
            raise TypeError("Lastname should contain letters only")
        
    def phonenumber_verification(self):
        if (len(self.phonenumber)==10):
            if type(self.phonenumber) == str:                                                                            #TYPE VALIDATION
                print("Phone number verified")
            else:
                raise TypeError("Phone number should contain only integers ")
        else:
            raise ValueError("phone number should not be grater than or lesser than 10")
        
    def emailid_verification(self):
        if type(self.emailid) == str:                                                                               #VALUE VALIDATION
            if len(self.emailid) <= 25:                                                                              
                print("Emailid verified")
            else:
                raise ValueError("Emailid should not contain more than 25 values")
        else:
            raise TypeError("Invalid emailid")    
        

    def groups_verification(self):
        if type(self.groups) == str:
            if len(self.groups) <= 10:                                                                              #LEN FUNCTION
                print("Groups verified")
            else:
                raise ValueError("Groups should contain lesser than or equal to 10 letters")
        else:
            raise TypeError("Groups should contain letters only")

    def dob_verification(self):
        if isinstance(self.dob,str):                                                                                #ISINSTANCE METHOD
            if len(self.dob) <= 10:                                                                                 #LEN FUNCTION
                print("DOB verified")
            else:
                raise ValueError("DOB should contain lesser than or equal to 10 letters")
        else:
            raise TypeError("DOB should contain numbers and symbols only")   
   


bharathwaj=phone_Contacts("bharath","waj","9884412975","bharathwaj@gmail.com","Friend","28/02/2002")
bharathwaj.open_phcontacts()
bharathwaj.firstname_verification()
bharathwaj.lastname_verification()
bharathwaj.phonenumber_verification()
bharathwaj.emailid_verification()
bharathwaj.groups_verification()
bharathwaj.dob_verification()



        
phone=[{"Firstname":"srini","Lastname":"vassan","Phno":9791035741,"Email_id":"srinivassan@gmail.com","Groups":"Family","DOB":"16/10/1973"},                                  #DICTIONARY INSIDE LIST
           {"Firstname":"kesav","Lastname":"santhosh","Phno":6282932275,"Email_id":"kesav@gmail.com","Groups":"Friends","DOB":"03/05/2001"},]


for i in phone:                                                                                                             #LOOPING
    for j,k in i.items():                                                                                                     #KEY VALUES LOOPING
        print(f"{j}:{k}")

    
