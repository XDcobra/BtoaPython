# BtoaPython

A Python implementation for btoa from javascript.
The Python result will exactly be the same, as using btoa from javascript.


## Problem
Because Python stores numbers as an infinite number of bits and Javascript store numbers as signed 32bit, the result for base64 encoding using window.btoa and base64.b64encode is different.
