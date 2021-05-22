import os
import sys
PATH=os.path.abspath('') 
sys.path.append(PATH)
from apscheduler.schedulers.blocking import BlockingScheduler
import main
scheduler = BlockingScheduler()
@scheduler.scheduled_job('interval', minutes=60)
def timer():
    print('uncode')
    main.run()
try:
    timer()
    scheduler.start() 
except KeyboardInterrupt:
    exit() 