import sys
#from pytodoist import todoist
import requests
import pathlib
import pickle
from getpass import getpass

current_dir = str(pathlib.Path(__file__).resolve().parent)

MANABA_PATH=current_dir+'/pickle/manaba'
class Manaba():
    def __init__(self):
        try:
            with open(MANABA_PATH, 'rb') as f:
                self.user = pickle.load(f)
        except:
            self.user={}
            self.user['userid']=input('UserId>>')
            self.user['password']=getpass('PassWord>>')
            with open(MANABA_PATH, 'wb') as f:
                pickle.dump(self.user , f)
            
    def get_tasks(self):
        r = requests.post("https://manabaunko.azurewebsites.net", data=self.user) #POST user data
        return r.json()

if __name__=='__main__':
    manaba=Manaba()
    print(manaba.get_tasks())