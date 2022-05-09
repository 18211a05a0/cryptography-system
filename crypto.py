def machine():
    key = 'abcdefghijklmnopqrstuvwxyz !'
    value = key[-1] + key[0:-1]

    encryptDict = dict(zip(key,value))
    decryptDict = dict(zip(value,key))

    message = input("please enter your secret mesage: ")
    mode = input("please enter the mode : Encode(E) OR Decode(D): ")

    if mode.upper() == 'E':
        newMessage = ''.join([encryptDict[letter]
                              for letter in message.lower()])
    elif mode.upper() == 'D':
        newMessage = ''.join([decryptDict[letter]
                              for letter in message.lower()])
    else:
        print("\nplease enter a correct choice")
    return newMessage
try:
    print(machine())
except:
   print("An exception error")

