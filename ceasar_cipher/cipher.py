
import string


class Ceasar:

    def __init__(self, text=str, order=int, mod=int):
        self.text = text
        self.order = order
        self.mod = mod

        if mod == 0:
            self.data = self.encrypt()
        elif mod == 1:
            self.data = self.decrypt()
        else:
            raise ValueError("Invalid mod")
    
    def encrypt(self):

        encrypted_data = ""

        for char in self.text:
            if char in string.ascii_letters:
                if char.isupper():
                    encrypted_data += chr((ord(char) + self.order - 65) % 26 + 65)
                else:
                    encrypted_data += chr((ord(char) + self.order - 97) % 26 + 97)
            else:
                encrypted_data += char
        
        return encrypted_data

    def decrypt(self):

        decrypted_data = ""

        for char in self.text:
            if char in string.ascii_letters:
                if char.isupper():
                    decrypted_data += chr((ord(char) - self.order - 65) % 26 + 65)
                else:
                    decrypted_data += chr((ord(char) - self.order - 97) % 26 + 97)
            else:
                decrypted_data += char
        
        return decrypted_data

    def __str__(self):
        return self.data