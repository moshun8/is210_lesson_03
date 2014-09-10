#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Date and Time"""

DAY = raw_input("What day is it? : ").lower()[slice(0,3)]
TIME = int(raw_input("What time is it? (ex: 0930): "))

if DAY == 'sat' or 'sun' or TIME > 0600:
	SNOOZE = True
else:
	SNOOZE = False