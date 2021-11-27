class Employee:
    company="Google " # it states that now, google is company for every employee
    
    def getsalary(self): # self ma get salary ko value return garne ho ..
        print(f"Salary for {self.company}  is {self.salary} for employer {self.name}")

subash=Employee()
subash.salary=1000000
subash.name="Subash"
subash.getsalary()


