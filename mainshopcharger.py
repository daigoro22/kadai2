from datetime import datetime
from pytz import timezone

class MainShopCharger:
  inserted_student_card=None
  latest_charge_date=None
  
  def insertStudentCard(self,card):
    MainShopCharger.inserted_student_card=card
  
  def chargeMoney(self,money):
    card=MainShopCharger.inserted_student_card
    
    if card==None:
      print("学生証が挿入されていません")
      return
    else:
      MainShopCharger.latest_charge_date=datetime.now(timezone('Asia/Tokyo'))
      card.account_balance=card.account_balance+money
      
  def printLatestChargeDate(self):
    if MainShopCharger.latest_charge_date!=None:
      print(MainShopCharger.latest_charge_date)
  
  def printAccountBalance(self):
    card=MainShopCharger.inserted_student_card
    if card==None:
      print("学生証が挿入されていません")
      return
    else :
      print("学生名:"+str(card.student_name))
      print("残高:"+str(card.account_balance))