# Web3.0_Pre-elim

For the loan service project, I thought of creting a password protected portal for both borrowers and lenders to check how much they owe and how much they need to collect. I used the concept of encapsulation, inheritance and abstraction. 

I  defined a parent class object to begin with which contained basic attributes of both lenders and borrowers i.e.
1. name
2. password

which contained get method for password, get item method to make objects and its attributes iterable and an abstracted represent method for printing the details of the users


Then i created the borrowers and lenders class which inherited the name and password attributes of the parent class.
I had to override the repr method of the parent class since they had more attributes than just name to be printed.

After that i created functions to
1. Calculate loan
2. operate payback
3. Add lenders and borrowers
4. login checks for both users
5. menu pages for both users
6. main menu for the entire program

The gui of the program is command line based. I had specific attributes like rate and password hidden as i didnt want the user to modify with what had beeen initialised already. However a set method can be added to change it by that user. As of now, one would have to create another user id to modify passwords and change rates of lenders.

---------------------------------------------------------------------------------------------------------------------------------------------------

"Is the loaning system that you implemented centralized or decentralized? Point out the demerit(s) of a centralized system."
--> The loaning system which i implemented is a decentralized one. The demerit of having a centralized system here would be that since the users here
have same level of leeadership so having a chain of command is unfruitful. 
