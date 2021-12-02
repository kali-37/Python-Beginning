class Employee:
    company="Google " # it states that now, google is company for every employee
    def getsalary(self): # self ma get salary ko value return garne ho ..
        print(f"Salary for {self.company} is {self.salary} for employer {self.name1}")
        print(f"Salary for {self.company} is {self.salary} for employer {self.name2}")
user=Employee()
user.salary=1000000
user.name1="Subash"
user.name2="Ram"
user.getsalary()


