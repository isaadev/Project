from tkinter import *

root = Tk()

# Encrypt a single character using a Caesar cipher.
# char - the character to encrypt (str).
# key - the number of characters to shift by (int).
# Returns the encrypted character (str).
def encrypt_char(char, key):
    if char == " ":
        return char
    
    k = ord(char)
    k -= 97
    k += key
    k %= 26
    k += 97
    return chr(k)

# Encrypt an arbitrary string using a Caesar cipher.
# message - the string to encrypt (str).
# key - the number of characters to shift by (int).
# Returns the encrypted message (str).
def encrypt(message, key):
    result = ""
    
    for char in message:
        result += encrypt_char(char, key)
    
    return result
# Given a string, construct a new string whose adjacent characters are transposed.
# (If the string has odd length, leave the last character unchanged.)
# message - the string to transpose (str).
# Returns the transposed string (str).
def transpose(message):
    result = ""
    
    for i in range(0, len(message), 1):
        
        # handle the last character when the length of `message` is odd:
        if len(message) % 2 == 1 and i == len(message) - 1:
            result += message[i]
          
        # if `i` is even, then `result[i]` should be `message[i + 1]`:
        elif i % 2 == 0:
            result += message[i + 1]
            
        # if `i` is odd, then `result[i]` should be `message[i - 1]`:
        else:
            result += message[i - 1]
            
    return result

# Creating a Label Widget
myLabel1 = Label(root, text="Password Modification")
myLabel2 = Label(root, text="Enter a password to encrypt:")
myLabel1.pack()
myLabel2.pack()
e = Entry(root, width= 30)
e.pack()
myLabel3 = Label(root, text="Enter the number of characters to shift by:")
myLabel3.pack()
k = Entry(root, width= 10)
k.pack()



def myClick():
    myLabel = Label(root, text="Your new, encrypted password is:")
   
    
    x = transpose(encrypt(str(e.get()), int(k.get())))
    myLabel1 = Label(root, text=x)
    myLabel.pack()
    myLabel1.pack()

myButton = Button(root, text="Encrypt", command=myClick)
#myButton2 = Button(root, text="Decrypt")
#myLabel1.grid(row=0, column=0)
#myLabel2.grid(row=1, column=5)
#myButton.grid(row=2, column=1)
#myButton2.grid(row=3, column=2)

myButton.pack()
root.mainloop()