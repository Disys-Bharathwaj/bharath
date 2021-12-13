import gp

Bharathwaj=gp.Google_pay("Bharathwaj@gmail.com","9884412975","bharathwaj")
Bharathwaj.open_gpay()
Bharathwaj.email_verification()
Bharathwaj.mobile_verification()
Bharathwaj.name_verification()
Bharathwaj.otp_verification(15698,15698)
Bharathwaj.Bank_verification()
Bharathwaj.PanCard_Verification()
Bharathwaj.set_Pin("5384")
Bharathwaj.Enter_your_Pin(3465,3465)

class Phone_pe(gp.Google_pay):                                                                                          #INHERITANCE
    def __init__(slef,Email_ID,Phone_number,Name):
        super().__init__(Email_ID,Phone_number,Name)

    def open_phonepe(self):
        print("Phone pe")
        
Bharathwaj=Phone_pe("bharathwaj@gmail.com","9884412975","bharathwaj")
Bharathwaj.open_phonepe()
Bharathwaj.mobile_verification()
Bharathwaj.name_verification()
Bharathwaj.otp_verification(780965,780965)
Bharathwaj.Bank_verification()
Bharathwaj.PanCard_Verification()
Bharathwaj.set_Pin("238790")
Bharathwaj.Enter_your_Pin(3564,3564)

googlepay=[  { "name":"bharathwaj","gpaynum":9884412975,"type":"personal","transaction":"regular"},
                          {"name":"kesav","gpaynum":6282932275,"type":"personal","transaction":"rare"},
                          {"name":"srinivassan","gpaynum":9791035741,"type":"personal","transaction":"regular"},
                          {"name":"rajaprabhu","gpaynum":8508890774,"type":"personal","transaction":"regular"},
                          {"name":"ahsik","gpaynum":6382421835,"type":"personal","transaction":"regular"},]

for i in googlepay:                                                                                                             #LOOPING
    for j,k in i.items():                                                                                                       #KEY VALUES LOOPING
        print(f"{j}:{k}")
    

