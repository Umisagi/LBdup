#!/usr/bin/python
#-*-coding: utf-8 -*-


import json
import sys
# define the function blocks
def hello():
    result = "สวัสดีเหี้ยไรสัส"
def haha():
    result = "ตลกเหรอ"
def test():
    result = "ทดสอบมาทั้งวันแล้วนะ"


# map the inputs to the function blocks
options = {"สวัสดี" : hello(),
           "หวัดดี" : hello(),
           "ดี" : hello(),
           "ดีจ้า" : hello(),
           "555" : haha(),
           "ทดสอบ" : test(),
           "test" : test(),
           " " : test(),
           }
if len(sys.argv) < 2:
  sys.exit(0)

message = sys.argv[1]

options[message]()

print ("%s" % result)
