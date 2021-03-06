#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 15 07:00:19 2022

@author: ousmanealhayri
"""
import sys
import json


def getMinConfidence():
    """ Get the minimum number of transaction occurrence for each itemset """

    try:
        with open("apriori_settings.json", "r") as j:
            configs = json.load(j)
        minconfidence = configs["minimum-support"]
    except:
        # A user-defined value
        minconfidence = 5
    return minconfidence


minconfidence = getMinConfidence()
addeditems = []
items = []

for line in sys.stdin:
    # Split the input
    combination, count = line.split("\t")
    count = int(count.replace("\n", ""))
    # Processing first occurrence of itemset
    if combination not in items:
        items.append(combination)
        addeditems.append([combination, count])
    # Processing repeated occurrence of itemset
    else:
        for i in range(0, len(items)):
            if items[i] == combination:
                addeditems[i][1] += 1

# Filter frequent item(sets)
for i in addeditems:
    if i[1] >= minconfidence:
        print("frequent" + '\t' + str(i))
    else:
        print("discarded" + '\t' + str(i[0]) + ',')
