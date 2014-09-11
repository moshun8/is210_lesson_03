#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Nested statements"""

BASE = raw_input(
    "Please pick between 2 colors - "
    "Seattle Gray or Manatee? : ")

if BASE == "Seattle Gray":
    ACCENT = raw_input("Ceramic Glaze or Cumulus Nimbus : ")
    if ACCENT == "Ceramic Glaze":
        HIGHLIGHT = raw_input("Basically White or White : ")
    elif ACCENT == "Cumulus Nimbus":
        HIGHLIGHT = raw_input("Off-White or Paper White : ")
elif BASE == "Manatee":
    ACCENT = raw_input("Platinum Mist of Spartan Sage : ")
    if ACCENT == "Platinum Mist":
        HIGHLIGHT = raw_input("Bone White or Just White : ")
    elif ACCENT == "Spartan Sage":
        HIGHLIGHT = raw_input("Fractal White or Not White : ")

print ("Your base color is {0}, your accent is {1}, and your highlight is {2}."
    ).format(BASE, ACCENT, HIGHLIGHT)