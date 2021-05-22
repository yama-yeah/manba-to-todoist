#!/usr/bin/env python

from collections import defaultdict
import sys
from typing import DefaultDict
from pytodoist import todoist
#import requests
import pathlib
import pickle
from getpass import getpass
import datetime

current_dir = str(pathlib.Path(__file__).resolve().parent)
TODOIST_PATH=current_dir+'/pickle/todoist'
class Todoist():
    def __init__(self):
        try:
            with open(TODOIST_PATH, 'rb') as f:
                self.token = pickle.load(f)
        except:
            self.token=getpass('API_Token>>')
            with open(TODOIST_PATH, 'wb') as f:
                pickle.dump(self.token , f)
        self.user = todoist.login_with_api_token(self.token)
        self.works = self.user.get_project('homework')
    def create_task(self,dic):
        task_dic={}
        course_name=list(dic.keys())
        for course in course_name:
            task_name=list(dic[course].keys())
            for task in task_name:
                end=dic[course][task]['end']
                end=datetime.datetime.strptime(end, '%Y-%m-%d %H:%M')
                end = end.strftime('%Y/%m/%d')
                task_dic[course+':'+task]=end
        return task_dic
    def get_tasks(self):
        return self.works.get_uncompleted_tasks()
        
    def check_complete(self,check,pushed):
        pushed_content=[vars(x)['content'] for x in pushed]
        check_content=[vars(x)['content'] for x in check]
        for i in range(len(pushed_content)):
            if(pushed_content[i] in check_content):
                #print(vars(pushed[i])['content'])
                self.delete_task(pushed[i])
            else:
                self.complete_task(pushed[i])
    def delete_task(self,task):
        
        
        task.delete()
    def complete_task(self,task):
        task.complete()
    def push_tasks(self,dic):
        check=[]
        task_dic=self.create_task(dic)
        tasks=list(task_dic.keys())
        pushed_task=self.get_tasks()
        for name in tasks:
            task=self.works.add_task(name,task_dic[name])
            check.append(task)
        self.check_complete(check,pushed_task)

if __name__=='__main__':
    todo=Todoist()
    todo.works.add_task('demo_task')
    task_demo=todo.get_tasks()[0]
    print(vars(task_demo)['content'])
    #content = name
    #due:date=date