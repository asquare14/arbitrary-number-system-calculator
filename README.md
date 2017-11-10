# arbitrary-number-system-calculator
A calculator with an arbitrary number system. An base-N arbitrary number system has N distinct digits, each of which could be 
an arbitrary numeric or special ([‘!@#$% ^&*()?|...])character. 
For example,NumberSystem(”123!”) would result in a base-4 number system where the values of the various characters will be 
{’1’7→0,’2’7→1, ’3’7→2,’!’7→3} . 
This calculator implements basic arithmetic operations and a number system convertervclass Converter(N1,N2) which takes 
two number systems N1 and N2. 
It has a method convert(n) which takes a number in number system N1 and returns its corresponding number in number
system N2.
It has also has a scientific module that implements a few scientific operations.
The GUI is handled by the Tkinter library.
