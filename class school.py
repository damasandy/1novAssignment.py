class school:
    def  __init__(self,name,num_of_students,location,is_public,tution_fee):
        self.name = name
        self.num_of_students = num_of_students
        self.location = location
        self.is_public = is_public
        self.tution_fee =tution_fee
school1 = school("GovernmentSchool",1000,"pokur",True,0.0)
school2 = school("PrivateSchool",500,"voletivaripalem",False,5000.0)
print(school1.name)
print(school1.num_of_students)
print(school1.location)
print(school1.is_public)
print(school1.tution_fee)

print(school2.name)
print(school2.num_of_students)
print(school2.location)
print(school2.is_public)
print(school2.tution_fee)