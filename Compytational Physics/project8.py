#!/usr/bin/env python
i = 0

while True:
    square = i ** 2
    if square > 80:
        break
    if square >= 10:
        print(square, end=' ')
    i += 1
