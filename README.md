# Custom Wordle Solver
## Introduction
This python script can be used to solve the word for any custom Wordle on mywordle.strivemath.com.
The URL of the custom Wordle includes a five character code at the end, which can then be
decrypted using the Vigenere cipher to reveal the word answer. The Vigenere cipher is a
method of encrypting alphabetic text by using a simple form of polyalphabetic substitution. 
Decryption requires knowledge of the keyword used during encryption, which in this case,
the keyword is WORDLE. This is accurate up to 23rd August 2023.

**python 3.11.4** was used for the development of the Custom Wordle Solver.
## Getting Started
Run the script, which will then prompt you to enter the five character code found at the end of the custom Wordle URL. It will then output the word answer! 

If the key ever changes, or you would like to use the script for anything else. Change the ```KEY``` constant within the code to the correct key.
## Known Issues
* Currently no known issues
## Author
* **Thomas Farrar**