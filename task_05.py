#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Compound Examples"""

from decimal import Decimal

NAME = raw_input("What is your name? ").title()
PRINCIPLE = int(raw_input(
    'What is the amount of your principle (amount being borrowed)? '))
YEARS = int(raw_input("For how many years is this loan being borrowed? "))
QUALIFIED = raw_input("Are you prequalified for this loan? ").upper()[:1]
INTEREST = 0

if PRINCIPLE <= 199999:
    if 1 <= YEARS <= 15:
        if QUALIFIED == "Y":
            INTEREST = float('.0363')
        elif QUALIFIED == "N":
            INTEREST = float('.0465')
        else:
            INTEREST = float('0.0')
    elif 15 < YEARS <= 20:
        if QUALIFIED == "Y":
            INTEREST = float('.0404')
        elif QUALIFIED == "N":
            INTEREST = float('.0498')
        else:
            INTEREST = float('0.0')
    elif 20 < YEARS <= 30:
        if QUALIFIED == "Y":
            INTEREST = float('.0577')
        elif QUALIFIED == "N":
            INTEREST = float('.0639')
        else:
            INTEREST = float('0.0')
elif 200000 <= PRINCIPLE <= 999999:
    if 1 <= YEARS <= 15:
        if QUALIFIED == "Y":
            INTEREST = float('.0302')
        elif QUALIFIED == "N":
            INTEREST = float('.0398')
        else:
            INTEREST = float('0.0')
    elif 15 < YEARS <= 20:
        if QUALIFIED == "Y":
            INTEREST = float('.0327')
        elif QUALIFIED == "N":
            INTEREST = float('.0408')
        else:
            INTEREST = float('0.0')
    elif 20 < YEARS <= 30 and QUALIFIED == "Y":
        INTEREST = float('.0466')
    else:
        INTEREST = float('0.0')
elif PRINCIPLE >= 1000000:
    if 1 <= YEARS <= 15 and QUALIFIED == "Y":
        INTEREST = float('.0205')
    elif 15 < YEARS <= 20 and QUALIFIED == "Y":
        INTEREST = float('.0262')
    else:
        INTEREST = float('0.0')
else:
    INTEREST = float('0.0')

PRINCIPLE = Decimal(PRINCIPLE)
INTEREST = Decimal(INTEREST)
YEARS = Decimal(YEARS)

TOTAL = Decimal(PRINCIPLE * (1+(INTEREST/12)) ** (12 * YEARS))
TOTAL = round(TOTAL)

if INTEREST == float('0.0'):
    TOT_REPO = None
    TOTAL = None
else:
    TOT_REPO = str('{0}{1:0,.0f}'.format('$', TOTAL))

PRIN_REPO = '{0}{1:0,.0f}'.format('$', PRINCIPLE)
YEAR_REPO = str(YEARS) + "yrs"

if QUALIFIED == 'Y':
    QUALIFIED = 'Yes'
else:
    QUALIFIED = 'No'

REPORT = (
    'Loan Report for: {0}'
    '\n{1}'
    '\n\tPrincipal:        {2:>10}'
    '\n\tDuration:         {3:>10}'
    '\n\tPre-Qualified?:   {4:>10}'
    '\n'
    '\n\tTotal:            {5:>10}'
    ).format(NAME, '-' * 68, PRIN_REPO, YEAR_REPO, QUALIFIED, TOT_REPO)

print REPORT