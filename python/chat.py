#!/usr/bin/python
#-*-coding: utf-8 -*-


import json
import sys
# define the function blocks
def hello():
    result = "สวัสดีเหี้ยไรสัส"
def haha():
    result = "ตลกเหรอ"
def even():
    print "n is an even number\n"
def prime():
    print "n is a prime number\n"

# map the inputs to the function blocks
options = {"สวัสดี" : hello,
           "หวัดดี" : hello,
           "ดี" : hello,
           "ดีจ้า" : hello,
           "555" : haha,
           "ทดสอบ" : test,
           "test" : test,
           " " : test,
           }
if len(sys.argv) < 2:
  sys.exit(0)

message = sys.argv[1]

option[message]()

print ("%s" % result)
