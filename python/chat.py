#!/usr/bin/python
#-*-coding: utf-8 -*-


import json
import sys

if len(sys.argv) < 2:
  sys.exit(0)

mes = sys.argv[1]
message = ''.join(chr(i) for i in mes)

if (message == "สวัสดี"):
    result = "สวัสดีครับ มีอะไรให้รับใช้ครับ"
elif (message == "สวัสดี ครับ"):
    result = "สวัสดีครับ มีอะไรให้รับใช้ครับ"
elif (message == "ลาก่อน"):
    result = "ลาก่อนครับ"
elif (message == "ควย"):
    result = "ไม่น่ารักเลยครับ"
else:
    result = "ระบบไม่สามารถประมวลผลคำที่ท่านส่งมาได้ ขออภัยด้วยครับ"

print (result+" "+message)
