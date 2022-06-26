# Assignment 2



### Pure View or None Functions

MulDiv and getCompoundInterest are pure functions as they do not read or modify any state variables and returns only using the parameters passed to it or using the local variables contained insde of it.

getOwnerBalance and viewDues are view functions as they are only reading and ensuring that the state variables state variables cannot be modified after calling them.

settleDues and reqLoan are niether view or pure as they modify the state variables contained within them.
