#!/usr/bin/python3

name_input = input("Enter your name: ")
user_name = name_input.split(" ")
initials = []
for x in user_name:
	initials.append(x[0])

print("".join(initials))
