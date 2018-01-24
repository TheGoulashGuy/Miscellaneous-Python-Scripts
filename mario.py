#!/usr/bin/python3

base = ['#','#']
brick = '#'

height = int(input("Pyramid height: "))

iterator = 1

print(base)

while iterator < height:
	base.insert(0,brick)
	print(str(base))
	iterator += 1
