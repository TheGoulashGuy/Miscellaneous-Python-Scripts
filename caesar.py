#!/usr/bin/python3

user_key = int(input("Enter encryption key: "))
user_msg = input("Enter the message: ")
user_msg = user_msg.upper()

alphabet = {'A':1,'B':2,'C':3,'D':4,'E':5,'F':6,'G':7,'H':8,'I':9,'J':10,'K':11,'L':12,'M':13,'N':14,'O':15,'P':16,'Q':17,'R':18,'S':19,'T':20,'U':21,'V':23,'W':24,'X':25,'Y':26,'Z':27}

encrypted_msg = []
decrypted_msg = []


def encrypt():
	for x in user_msg:
		letter_to_encrypt = alphabet.get(x)
		print(letter_to_encrypt)
		encrypted_letter = alphabet.get(letter_to_encrypt + user_key)
		letter_to_append = alphabet[encrypted_letter]
		print(letter_to_append)
		encrypted_msg.append(letter_to_append)

	print(encrypted_msg)

encrypt()
		



