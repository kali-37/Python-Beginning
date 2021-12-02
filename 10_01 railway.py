class RailWayForm: # class chainxa rw it;s for railway form 
    formType="RailWayForm"
    # self is like class for given data of class
    
    def printData(self):
        print(f"Name is {self.name}")
        print(f"Address is {self.address}")
        print(f"Sex is {self.sex}")
        print(f"Age is {self.age}")
        print(f"Status is {self.status}")
        print(f"{self.formType}")

subashApplication=RailWayForm()
subashApplication.name="Subash"
subashApplication.address="Amarshing,Pokhara"
subashApplication.sex="Male Sigma"
subashApplication.age="19"
subashApplication.status="unmaried"
subashApplication.printData() # now it takes to function at line n.b 3 it is now
