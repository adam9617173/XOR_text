class Crypto:
    def __init__(self, style = None, key = None):
        self.key = list(key)
        self.style = style
        self.msg = None
        self.ans = None
    
    def Encrypt(self, msg):
        if self.style == "XOR":
            self.msg = list(msg)
            save = list()
            for i in range(len(self.msg)):
                save.append(int(self.msg[i])^int(self.key[i]))

            self.ans = save

        elif  self.style == "Caesar":
            self.msg = list(msg)
            key_len = len(self.key)
            save = list()
            for i in range(len(self.msg)):
                save.append(chr(ord(self.msg[i])+int(self.key[i%key_len])))    
            self.ans = save

    def Decrypt(self, ans):
        if style == "XOR":
            self.ans = list(ans)
            save = list()
            for i in range(len(self.ans)):
                save.append((int(self.ans[i])^int(self.key[i])))

            self.msg = save        
        elif style == "Caesar":
            key_len = len(self.key)    


    def lists(self):
        print("now keys is : ",self.key)
        print("now msg is : ", self.msg)
        print("now ans is : ", self.ans)

