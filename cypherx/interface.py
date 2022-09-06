import os
from rich import print
import time
import cypherx

class StartTUI:

    def cls(self):
        os.system('cls' if os.name=='nt' else 'clear')

    def __init__(self) -> None:

        self.terminalUI()

    def presentation(self, cipher: int = 0) -> str:

        self.banner = str("\n[bold green] ▄████▄▓██   ██▓ ██▓███   ██░ ██ ▓█████  ██▀███  ▒██   ██▒\n" +
            "▒██▀ ▀█ ▒██  ██▒▓██░  ██▒▓██░ ██▒▓█   ▀ ▓██ ▒ ██▒▒▒ █ █ ▒░\n" +
            "▒▓█    ▄ ▒██ ██░▓██░ ██▓▒▒██▀▀██░▒███   ▓██ ░▄█ ▒░░  █   ░\n" +
            "▒▓▓▄ ▄██▒░ ▐██▓░▒██▄█▓▒ ▒░▓█ ░██ ▒▓█  ▄ ▒██▀▀█▄   ░ █ █ ▒\n" +
            "▒ ▓███▀ ░░ ██▒▓░▒██▒ ░  ░░▓█▒░██▓░▒████▒░██▓ ▒██▒▒██▒ ▒██▒\n" +
            "░ ░▒ ▒  ░ ██▒▒▒ ▒▓▒░ ░  ░ ▒ ░░▒░▒░░ ▒░ ░░ ▒▓ ░▒▓░▒▒ ░ ░▓ ░\n" +
            "  ░  ▒  ▓██ ░▒░ ░▒ ░      ▒ ░▒░ ░ ░ ░  ░  ░▒ ░ ▒░░░   ░▒ ░\n" +
            "░       ▒ ▒ ░░  ░░        ░  ░░ ░   ░     ░░   ░  ░    ░\n" +  
            "░ ░     ░ ░               ░  ░  ░   ░  ░   ░      ░    ░\n" +  
            "░       ░ ░                                               [/bold green]")

        welcome = str("\n Welcome to [link=https://github.com/yuritorresf/cypherx.git][green]CypherX[/green][/link], a simple and easy to use cryptography program.\n\n")
        
        menu = str("")
        
        if cipher == 1:
            menu = str(" Choice an option: \n\n[bold] 1 - Encrypt \n 2 - Decrypt \n 3 - Force Decrypt \n 0 - [red]Back[/red]\n[/bold]")
        elif cipher == 2:
            menu = str(" Choice an option: \n\n[bold] 1 - Encrypt \n 2 - Decrypt \n 0 - [red]Back[/red]\n[/bold]")
        else:
            menu = str(" Choice an option: \n\n[bold] 1 - Caesar \n 2 - Atbash \n 0 - [red]Exit[/red]\n[/bold]")

        print(self.banner + welcome + menu)


    def CaesarTUI(self):
        try:
            try:
                self.cls()
                
                self.presentation(1)

                caesar_choice = int(input("\n [=] Enter your choice: "))
                if caesar_choice == 1:
                    self.cls()
                    print(self.banner)
                    print(" Caesar Cipher - Encrypt\n")
                    text = input(" [+] Enter the text: ")
                    order = int(input(" [+] Enter the key: "))
                    print(" [-] Encrypted text: " + str(cypherx.Caesar(text, order, 0)))

                    key = input("\n [!] Press any key to continue...")
                
                    if key != "":
                        caesar_choice = 0
                        pass
                    
                elif caesar_choice == 2:
                    self.cls()
                    print(self.banner)
                    print(" Caesar Cipher - Decrypt\n")
                    text = input(" [+] Enter the text: ")
                    order = int(input(" [+] Enter the key: "))
                    print(" [-] Decrypted text: " + str(cypherx.Caesar(text, order, 1)))

                    key = input("\n [!] Press any key to continue...")
                
                    if key != "":
                        caesar_choice = 0
                        pass

                elif caesar_choice == 3:
                    self.cls()
                    print(self.banner)
                    print(" Caesar Cipher - Force Decrypt\n")
                    text = input(" [+] Enter the text: ")
                    print()
                    caesar = cypherx.Caesar(text, 0, 2).force()
                    for c in caesar:
                        print(" [-] Decrypted text: " + str(c))

                    key = input("\n [!] Press any key to continue...")
                
                    if key != "":
                        caesar_choice = 0
                        pass

                elif caesar_choice == 0:
                    self.cls()
                
                self.cls()

            except ValueError:
                print(" [!] Invalid value. Try again. Caesar Cipher Menu")

        except KeyboardInterrupt:
            print("\n\n Cypherx ended!")

    def AtbashTUI(self):
        try:
            try:
                self.cls()

                self.presentation(1)
                
                atbash_choice = int(input("\n [=] Enter your choice: "))
                    
                if atbash_choice == 1:
                    self.cls()
                    print(self.banner)
                    print(" Atbash Cipher - Encrypt\n")
                    text = input(" [+] Enter the text: ")
                    print(" [-] Encrypted text: " + str(cypherx.Atbash(text, 0)))

                    key = input("\n Press any key to continue...")
                
                    if key != "":
                        atbash_choice = 0
                        pass
                    
                elif atbash_choice == 2:
                    self.cls()
                    print(self.banner)
                    print(" Atbash Cipher - Decrypt\n")
                    text = input(" [+] Enter the text: ")
                    print(" [-] Decrypted text: " + str(cypherx.Atbash(text, 1)))

                    key = input("\n [!] Press any key to continue...")
                
                    if key != "":
                        atbash_choice = 0
                        pass

                elif atbash_choice == 0:
                    self.cls()
                    
                self.cls()

            except ValueError:
                print(" [!] Invalid value. Try again. Atbash Cipher Menu")

        except KeyboardInterrupt:
            print("\n\n Cypherx ended!")

    def terminalUI(self):

        try:
            
            choice = 9

            while choice != 0:
                choice = None

                self.presentation()
                
                try:
                    choice = int(input(" [=] Enter your choice: "))
                except ValueError:
                    self.cls()
                    print(self.banner + '\r\n [!] Invalid option, try again.', end='', flush=True)
                    time.sleep(1)
                    self.cls()
                if choice == 1:
                    self.CaesarTUI()

                elif choice == 2:
                    self.AtbashTUI()

                elif choice == 0:
                    print("\n Cypherx ended!\n")
                    break

        except KeyboardInterrupt:
            print("\n\n Cypherx ended!")

class CLI:
    
    def __init__(self, classcipher: str = "", message: str = "", key = None, cipher: str = "", method: str = "verbose", encdec: str = "encrypt") -> str:
        
        self.__version__ = '1.3.1'
        
        self.classcipher = classcipher
        self.message = message
        self.key = key
        self.cipher = cipher
        self.method = method
        self.encdec = encdec

        self.cipher_dict = {
            "caesar": "Caesar",
            "atbash": "Atbash"
        }

        self.method_dict = {
            "normal": "Normal",
            "verbose": "Verbose",
            "quiet": "Quiet"
        }

        self.encdec_dict = {
            "encrypt": "Encrypt",
            "decrypt": "Decrypt"
        }

    def banner(self):
        banner = f"[bold gray]\nCypherX version {self.__version__}[/bold gray]. [bold red]{self.cipher_dict[self.cipher]}[/bold red] cipher, [bold green]{str(self.encdec_dict[self.encdec]).lower()}[/bold green] method in [bold yellow]{str(self.method_dict[self.method]).lower()}[/bold yellow] mode.\n"
        print(banner)

    def showResult(self):
        
        msgwelcome = f"[bold][\N{check mark}] Message {str(self.encdec_dict[self.encdec])}ed successfully![/bold]"
        msg        = f"\n[gray][+] Message:[/gray] [bold yellow]{self.message}[/bold yellow]"
        encdecmsg  = f"[gray][=] {str(self.encdec_dict[self.encdec])}ed message:[/gray] [bold green]{self.classcipher}[/bold green]"
        key        = f"[gray][+] Key/Order:[/gray] [bold orange]{self.key}[/bold orange]"
        done       = f"\n[gray][\N{check mark}][/gray][bold green] Done![/bold green]\n"

        if self.method == "normal": # Normal
            print(msgwelcome, end="\n", flush=True)
            print(encdecmsg)
            print(done)
        elif self.method == "verbose": # Verbose
            print(msgwelcome, end="\n", flush=True)
            print(msg)
            if self.cipher == "caesar": # Caesar
                print(key)
            print(encdecmsg)
            print(done)
        elif self.method == "quiet": # Quiet
            print(f"[bold cyan]{self.message}[/bold cyan]")