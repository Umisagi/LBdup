#!/usr/bin/python
#-*-coding: utf-8 -*-

import aiml
import json
import sys

if len(sys.argv) < 2:
  sys.exit(0)

message = sys.argv[1]

kernel = aiml.Kernel()
kernel.learn("std-startup.xml")
kernel.respond("load aiml b")

if(message == "555"):
  result = "ขำ";
else:
  result = "ยังไม่ได้ตั้งค่าไว้";
print ("%s" % result)
