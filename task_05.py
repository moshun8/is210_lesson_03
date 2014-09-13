#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Compound Examples"""

from decimal import Decimal

NAME = raw_input("What is your name? ")
PRINCIPLE = int(raw_input(
    'What is the amount of your principle (amount being borrowed)? '))
YEARS = int(raw_input("For how many years is this loan being borrowed? "))
QUALIFIED = raw_input("Are you prequalified for this loan? ").title()
INTEREST = 0

if PRINCIPLE <= 199999:
    if 1 <= YEARS < 15:
        if QUALIFIED == "Yes":
            INTEREST = float('.0363')
        elif QUALIFIED == "No":
            INTEREST = float('.0465')
        else:
            INTEREST = float('0.0')
    elif 15 <= YEARS < 20:
        if QUALIFIED == "Yes":
            INTEREST = float('.0404')
        elif QUALIFIED == "No":
            INTEREST = float('.0498')
        else:
            INTEREST = float('0.0')
    elif 20 <= YEARS <= 30:
        if QUALIFIED == "Yes":
            INTEREST = float('.0577')
        elif QUALIFIED == "No":
            INTEREST = float('.0639')
        else:
            INTEREST = float('0.0')
elif 200000 <= PRINCIPLE <= 999999:
    if 1 <= YEARS < 15:
        if QUALIFIED == "Yes":
            INTEREST = float('.0302')
        elif QUALIFIED == "No":
            INTEREST = float('.0398')
        else:
            INTEREST = float('0.0')
    elif 15 <= YEARS < 20:
        if QUALIFIED == "Yes":
            INTEREST = float('.0327')
        elif QUALIFIED == "No":
            INTEREST = float('.0408')
        else:
            INTEREST = float('0.0')
    elif 20 <= YEARS <= 30 and QUALIFIED == "Yes":
        INTEREST = float('.0466')
    else:
        INTEREST = float('0.0')
elif PRINCIPLE >= 1000000:
    if 1 <= YEARS < 15 and QUALIFIED == "Yes":
        INTEREST = float('.0205')
    elif 15 <= YEARS <= 20 and QUALIFIED == "Yes":
        INTEREST = float('.0262')
    else:
        INTEREST = float('0.0')
else:
    INTEREST = float('0.0')

TOTAL = round(Decimal(PRINCIPLE * (1+(INTEREST/12)) ** (12 * YEARS)))

if INTEREST == float('0.0'):
    TOTAL = None
    TOT_REPO = None
else:
    TOT_REPO = ('{0}{1:0,.0f}').format('$', TOTAL)
    

PRIN_REPO = ('{0}{1:0,.0f}').format('$', PRINCIPLE)
# TOT_REPO = ('{0}{1:0,.0f}').format('$', TOTAL)
YEAR_REPO = str(YEARS) + "yrs"
REPORT = (
    'Loan Report for: {0}'
    '\n{1}'
    '\n\tPrincipal:        {2}'
    '\n\tDuration:         {3}'
    '\n\tPre-Qualified?:   {4}'
    '\n'
    '\n\tTotal:            {5}'
    ).format(NAME, '-' * 68, PRIN_REPO, YEAR_REPO, QUALIFIED, TOT_REPO)

print REPORT