#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Compound Examples"""

from decimal import Decimal

NAME = raw_input("What is your name? ")
PRINCIPLE = int(raw_input('What is the amount of your principle '
    '(amount being borrowed)? '))
YEARS = int(raw_input("For how many years is this loan being borrowed? "))
QUALIFIED = raw_input("Are you prequalified for this loan? ").title()

if PRINCIPLE <= 199999:
    if 1 <= YEARS < 15:
        if QUALIFIED == "Yes":
            INTEREST = Decimal('.0363')
        elif QUALIFIED == "No":
            INTEREST = Decimal('.0465')
    elif 15 <= YEARS < 20:
        if QUALIFIED == "Yes":
            INTEREST = Decimal('.0404')
        elif QUALIFIED == "No":
            INTEREST = Decimal('.0498')
    elif 20 <= YEARS <= 30:
        if QUALIFIED == "Yes":
            INTEREST = Decimal('.0577')
        elif QUALIFIED == "No":
            INTEREST = Decimal('.0639')
elif 200000 <= PRINCIPLE <= 999999:
    if 1 <= YEARS < 15:
        if QUALIFIED == "Yes":
            INTEREST = Decimal('.0302')
        elif QUALIFIED == "No":
            INTEREST = Decimal('.0398')
    elif 15 <= YEARS < 20:
        if QUALIFIED == "Yes":
            INTEREST = Decimal('.0327')
        elif QUALIFIED == "No":
            INTEREST = Decimal('.0408')
    elif 20 <= YEARS <= 30 and QUALIFIED == "Yes":
        INTEREST = Decimal('.0466')
elif PRINCIPLE >= 1000000:
    if 1 <= YEARS < 15 and QUALIFIED == "Yes":
        INTEREST = Decimal('.0205')
    elif 15 <= YEARS <= 20 and QUALIFIED == "Yes":
        INTEREST = Decimal('.0262')

TOTAL = PRINCIPLE * (1+(INTEREST/1)) ** YEARS
REPORT = ('Loan Report for: {0}\n{1}\n\tPrincipal:  ${2:0,.0f}'
    '\n\tDuration: {3}yrs\n\tPre-Qualified?: {4}\n\n\tTotal: ${5:0,.0f}'
    ).format(NAME, '-' * 68, PRINCIPLE, YEARS, QUALIFIED, TOTAL)

print REPORT
