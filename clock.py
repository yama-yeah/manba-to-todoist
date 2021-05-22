import os
import sys
PATH=os.path.abspath('') 
sys.path.append(PATH)
from apscheduler.schedulers.blocking import BlockingScheduler
import main
sched = BlockingScheduler(timezone="UTC")
@sched.scheduled_job('interval',
                     minutes=60)
def exe():
    main.run()
sched.start()  