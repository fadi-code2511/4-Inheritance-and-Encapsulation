class User:
    def __init__(self,name,email):
       self.__name=name
       self.__email=email

    def get_info(self):
      return f"name: {self.__name},email: {self.__email}"  

    def set_email(self,newEmail):
      self.__email=newEmail
      return self.__email