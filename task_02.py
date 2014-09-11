#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Conditionals with raw_input and blood pressure"""

BP_STATUS = int(raw_input("What is your blood pressure? : "))

if BP_STATUS <= 90:
    BP_STATUS = "Low"
elif BP_STATUS > 90 and BP_STATUS <= 119:
    BP_STATUS = "Ideal"
elif BP_STATUS > 119 and BP_STATUS <= 139:
    BP_STATUS = "Warning"
elif BP_STATUS > 139 and BP_STATUS <= 160:
    BP_STATUS = "High"
elif BP_STATUS > 160:
    BP_STATUS = "Emergency"

print "Your status is {0}.".format(BP_STATUS)