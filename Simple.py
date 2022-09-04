import os
if __name__ == "__main__":
   try:
       os.system('git pull')
       os.system('mkdir OK')
       os.system('mkdir CP')
       __import__("Simple").login()
   except Exception as e:
       exit(str(e))
