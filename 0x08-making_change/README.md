# Making Change

## Problem statement
You are given a pile of coins of different values and your goal is to determine the fewest number of coins needed to meet a given amount total. Write a Python function ```makeChange(coins, total)``` that takes in two parameters:
```coins```: a list of integers representing the values of the coins in your possession. You can assume that you have an infinite number of each denomination of coin in the list. The value of a coin will always be an integer greater than 0.
```total```: an integer representing the total amount that needs to be reached using the available coins.
The function should return the fewest number of coins needed to meet the total amount. If the total amount is 0 or less, the function should return 0. If the total amount cannot be met by any number of coins you have, the function should return -1.