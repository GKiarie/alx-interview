UTF-8 Validation

Qn:
Write a method that determines if a given data set represents a valid UTF-8 encoding.

Prototype: def validUTF8(data)
Return: True if data is a valid UTF-8 encoding, else return False
A character in UTF-8 can be 1 to 4 bytes long
The data set can contain multiple characters
The data will be represented by a list of integers
Each integer represents 1 byte of data, therefore you only need to handle the 8 least significant bits of each integer

******
soln
******

The UTF-8 encoding rules are as follows:

->A character in UTF-8 can be 1 to 4 bytes long.
->If a character is represented in multiple bytes, the first byte will have a specific pattern indicating the number of bytes that follow.
->Each byte (8 least significant bits) will have a specific pattern that identifies whether it's a continuation byte or the first byte of a character.

resources:
https://www.youtube.com/watch?v=MijmeoH9LT4
https://en.wikipedia.org/wiki/UTF-8


*******
test
********
carrie@ubuntu:~/0x04-utf8_validation$ ./0-main.py
True
True
False