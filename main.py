import os
import sys
PATH=os.path.abspath('') 
sys.path.append(PATH)
from manaba import Manaba
from todoist import Todoist

def run():
    todo=Todoist()
    mana=Manaba()
    dic=mana.get_tasks()
    todo.push_tasks(dic)
if __name__ == "__main__":
    run()