from conversion import conversion

class result(conversion):

    def __init__(self):        
        usr_action = input("""
            1. Cm to Ft
            2. Km to Miles
            3. Usd to Inr
            4. Exit\n""")
        
        if usr_action == "4":
            print("\nThank You")

        elif usr_action == "3":
            self.usr_value = float(input("Enter Usd:"))
            print(f"\n{self.usr_value}usd to inr: ", self.usd_inr(self.usr_value))

        elif usr_action == "2":
            self.usr_value = float(input("Enter Km:"))
            print(f"\n{self.usr_value}km to miles: ", self.km_miles(self.usr_value))

        elif usr_action == "1":
            self.usr_value = float(input("Enter Cm:"))
            print(f"\n{self.usr_value}cm to ft: ", self.cm_ft(self.usr_value))
    
#Next is to add an interface