#error handling
try:
      with open("some_file.txt") as f:
            print(f)
         
except FileNotFoundError as e:
      print("FileNotFoundError      ", e)

except ZeroDivisionError as e:
      print("ZeroDivisionError      ", e)
      
except:
      print("something went wrong... lo nora - hakol tov")

else:
      print("everything is cool!")

finally:
      print("TAMID!!!!")


      
