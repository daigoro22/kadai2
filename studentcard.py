from PIL import Image, ImageDraw, ImageFont

class StudentCard:
    card_list=[]
    __account_balance=0
    __student_name=""
    __student_num=0
    __artist_name=""
    __artist_words=[]
    __student_image=None
    
    @property
    def account_balance(self):
        return self.__account_balance
    
    @account_balance.setter
    def account_balance(self,balance):
      if type(balance) is int:
        self.__account_balance=balance
      
    @property
    def student_name(self):
        return self.__student_name
      
    @student_name.setter
    def student_name(self,name):
      if type(name) is str :
        self.__student_name=name
        
    @property
    def student_num(self):
      return self.__student_num
    
    @student_num.setter
    def student_num(self,num):
      if type(num) is int:
        self.__student_num=num
        
    @property
    def artist_name(self):
      return self.__artist_name
    
    @artist_name.setter
    def aritst_name(self,name):
      if type(name) is str:
        self.__artist_name=name
    
    @property
    def artist_words(self):
      return self.__artist_words
    
    @artist_words.setter
    def aritst_words(self,words):
      if isinstance(words,list):
        for word in words:
          if word is not str:
            return
        self.__artist_words=words
      
    @property
    def student_image(self):
      return self.__student_image
    
    @student_image.setter
    def student_image(self,image):
      self.__student_image=image
    
    def __init__(self,name,num,artist,words,image_loc):
      StudentCard.card_list.append(self)
      self.__student_name=name
      self.__student_num=num
      self.__artist_name=artist
      self.__artist_words=words
      self.__student_image = Image.open(image_loc)