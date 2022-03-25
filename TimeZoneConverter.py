from datetime import datetime
import pytz
  
original = pytz.timezone('Asia/Kolkata')
converted = pytz.timezone('America/Chicago')
converted1=pytz.timezone('Australia/Adelaide')
converted2=pytz.timezone('Europe/Paris')
converted3=pytz.timezone('Africa/Lagos')
converted4=pytz.timezone('America/Rio_Branco')
  
def main():
      print("You are using IST time Zone")

      dateTimeObj = datetime.now(original)
      print("IST Time(Kolkata): ",
      dateTimeObj.strftime(' %H:%M:%S %Z %z'))
  
      while(True):
            print("Press 1 for Chicago,2 for Adelaide,3 for Paris,4 for Lagos,5 for Rio-Branco")
            choice=int(input("Enter your choice No "))

            if choice == 1:
                  dateTimeObj = datetime.now(converted )
                  print("USA Time(Chicago): ",
                  dateTimeObj.strftime(' %H:%M:%S %Z %z'))

            elif choice == 2:
                  dateTimeObj = datetime.now(converted1 )
                  print("Australia Time(Adelaide): ",
                  dateTimeObj.strftime(' %H:%M:%S %Z %z')) 

            elif choice == 3:
                  dateTimeObj = datetime.now(converted2 )
                  print("France Time(Paris): ",
                  dateTimeObj.strftime(' %H:%M:%S %Z %z'))

            elif choice == 4:
                  dateTimeObj = datetime.now(converted3 )
                  print("Nigeria Time(Lagos): ",
                  dateTimeObj.strftime(' %H:%M:%S %Z %z')) 

            elif choice == 5:
                  dateTimeObj = datetime.now(converted4 )
                  print("Brazil Time(Rio-Branco): ",
                  dateTimeObj.strftime(' %H:%M:%S %Z %z'))  

            else:
                  print("Enter A Valid No")
                  choice=int(input("Enter your choice No "))          

            print("\n")
            print("*" * 50)
            print("\n")
main()                  