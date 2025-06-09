# Task 4 - Performance Optimization Report

## 🔧 Original Problem
- Calculating sum of squares of even numbers up to `n`
- Used a `for` loop with `if` condition inside
- Unnecessary checks made it slower

## 🔁 Refactored Solution
- Used `range(2, n+1, 2)` to skip odd numbers
- Used generator expression inside `sum()` for better memory and speed

## ⏱️ Performance Gain
- Improved readability and performance
- Removed extra condition checking
- Faster execution with clean syntax
