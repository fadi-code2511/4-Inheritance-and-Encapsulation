class User:
    def __init__(self,name,email):
       self.__name=name
       self.__email=email

    def get_info(self):
      return f"name: {self.__name},email: {self.__email}"  

    def set_email(self,newEmail):
      self.__email=newEmail
      return self.__email
    
class Student(User):
  def __init__(self, name, email):
      super().__init__(name,email)
      self.__enrolled_courses=[]

  def enroll(self,course_name):
    self.__enrolled_courses.append(course_name)
  
  def get_enrolled_courses(self):
    return self.__enrolled_courses
  
class Instructor(User):
  def __init__(self,name,email):
    self.__teaching_courses=[]
    super().__init__(name,email)

  def add_course(self,course_name):
    self.__teaching_courses.append(course_name)
  
  def get_added_course(self):
    return self.__teaching_courses
  
# name1=User("fadi","nasr@gmail.com")
# name1.get_info()
# name1.set_email("you@yahoo.com")
# name1.get_info()
# student1=Student("sami","sami@gmail.com")
# student1.enroll("physics")
# student1.get_info()
Instructor1=Instructor("jad","jad@gmail.com")
Instructor1.get_info()
Instructor1.add_course("science")
Instructor1.get_info()
print(Instructor1.get_added_course())
