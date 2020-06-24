#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May  8 11:47:28 2020

@author: linhaohong
"""
import matplotlib.pyplot as plt

temperature=[23.5,25.5,26.7,34,27,28,30,]
week=['周一','周二','周三','周四','周五','周六','周日',]
fig = plt.figure(figsize=(20, 8), dpi=100)
plt.plot(week,temperature)
plt.grid(color="y")
plt.show()