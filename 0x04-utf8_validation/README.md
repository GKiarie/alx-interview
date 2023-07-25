UTF-8 Validation
The UTF-8 encoding rules are as follows:

->A character in UTF-8 can be 1 to 4 bytes long.
->If a character is represented in multiple bytes, the first byte will have a specific pattern indicating the number of bytes that follow.
->Each byte (8 least significant bits) will have a specific pattern that identifies whether it's a continuation byte or the first byte of a character.