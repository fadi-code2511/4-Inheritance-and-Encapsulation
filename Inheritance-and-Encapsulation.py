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