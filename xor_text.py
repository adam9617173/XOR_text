import Demo

#key = 00111000
#msg = 01010011
#ans = 01101011

# dm = Demo.Crypto("00111000")
# print(dm.Encrypt("01010011"))
# print(dm.Decrypt("01101011"))

# a = input("Please input your keys first : ")
# demo = Demo.Crypto(a)
while(1):
    style = input("Choose Crypt or check list? \nPlease input XOR or Caesar or L (List): ")
    if style == "XOR" or style == "Caesar":
        key = input("Please input you crypt's key : ")
        demo = Demo.Crypto(style,key)
    elif style == "L" or style == "l":
        demo.lists()
        continue

    menu = input("\n\nE = encrypt \n\nD = Decrypt \n\nL = List \n\nQ = Quit \n\nPlease input the funtoin u want to use : ")
    if menu == "E" or menu == "e":
        msg = input("Please input your msg : ")
        demo.Encrypt(msg)

    elif menu == "D" or menu == "d":
        ans = input("Please input your ans : ")
        demo.Decrypt(ans)

    

    if menu == "Q" or menu == "q":
        break