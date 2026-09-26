# PLP Python Week 3

This repository contains my Week 3 assignment on Python conditions and loops.

## Files

### grade_reporter.py
This program uses a for loop, if/elif/else conditions, a running total, and a counter to calculate grades, passed students, failed students, and the average score.

### bug_hunt.py
This program demonstrates debugging a while loop. It contains fixes for a syntax error, a string concatenation error, and an off-by-one logic error.

## Reflection

The most challenging bug to track down was the off-by-one error in the while loop because the program ran without producing an error message.

I caught the logical error by checking the output against the expected sum of the numbers from 1 to 5. The program returned 10 instead of 15, which showed that one number was missing. I checked the loop boundary and changed `count < 5` to `count <= 5` so that 5 would also be included.
