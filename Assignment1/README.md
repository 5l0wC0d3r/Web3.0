The program basically takes input of a string and adds a number to it. And then hashes it as per the SHA256 protocol and returns the output in a byte string.
The byte string is converted into a hex string and its values are compared. 
when the hex is less than or equal to the target value, our nonce value is generated and time is noted.  
The output of the program is the Nonce value and time taken. 
