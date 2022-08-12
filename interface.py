import cipher as cp
import os

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

class InterfaceLaucher:

    def __init__(self, argv):
        
        # @commands
        #
        # --help ou -h    : Lista os comandos disponíveis no programa via argumentos
        # --encrypt ou -e : Encripta um texto via argumentos
        # --decrypt ou -d : Decripta um texto via argumentos
        # --force ou -f   : Força a decifragem de um texto via argumentos
        # --order ou -o   : Define a ordem da cifragem via argumentos
        # --version ou -v : Exibe a versão do programa via argumentos
        # --author ou -a  : Exibe o autor do programa via argumentos
        # --license ou -l : Exibe a licença do programa via argumentos

        self.commands = ['--help','--encrypt','--decrypt','--force','--order','--version','--author','--license','-h','-e','-d','-f','-o','-v','-a','-l'] # Lista de comandos disponíveis no programa
        self.argv = argv # Argumentos passados pelo usuário

        if len(self.argv) <= 1:
            self.terminalUI()
        elif len(self.argv) > 1 and len(self.argv) <= 5:
            self.lineUI()


    def lineUI(self):
        if self.argv[1] in self.commands:

            if "-e" in self.argv or "--encrypt" in self.argv and len(self.argv) == 5:
                try:
                    index = self.argv.index("-e")
                except:
                    index = self.argv.index("--encrypt")
            
                text = self.argv[index + 1]
                
                if text in self.commands:
                    print("\nInvalid syntax")
                else:
                    if "-o" in self.argv or "--order" in self.argv:

                        try:
                            index = self.argv.index("-o")

                        except:
                            index = self.argv.index("--order")

                        try:
                            order = int(self.argv[index + 1])
                        except:
                            print("\nInvalid syntax")
                            exit()

                        if order in self.commands:
                            print("\nInvalid syntax")
                        
                        else:
                            cipher = cp.Ceasar(text, order, 0)
                            print(cipher)
            
            elif "-d" in self.argv or "--decrypt" in self.argv:
                try:
                    index = self.argv.index("-d")
                except:
                    index = self.argv.index("--decrypt")
            
                text = self.argv[index + 1]
                
                if text in self.commands:
                    print("\nInvalid syntax")

                else:
                    if "-o" in self.argv or "--order" in self.argv:

                        try:
                            index = self.argv.index("-o")

                        except:
                            index = self.argv.index("--order")

                        try:
                            order = int(self.argv[index + 1])
                        except:
                            print("\nInvalid syntax")
                            exit()

                        if order in self.commands:
                            print("\nInvalid syntax")
                        
                        else:
                            cipher = cp.Ceasar(text, order, 0)
                            print(cipher)

            elif "-f" in self.argv or "--force" in self.argv:
                try:
                    index = self.argv.index("-f")
                except:
                    index = self.argv.index("--force")
            
                text = self.argv[index + 1]
                
                if text in self.commands:
                    print("\nInvalid syntax")

                else:
                    for x in range(1, 27):
                        cipher = cp.Ceasar(text, x, 1)
                        print(cipher)

    def terminalUI(self):

        print("\n\n    ██████╗███████╗ █████╗ ███████╗ █████╗ ██████╗\n" +
            "   ██╔════╝██╔════╝██╔══██╗██╔════╝██╔══██╗██╔══██╗\n" +
            "   ██║     █████╗  ███████║███████╗███████║██████╔╝\n" +
            "   ██║     ██╔══╝  ██╔══██║╚════██║██╔══██║██╔══██╗\n" +
            "   ╚██████╗███████╗██║  ██║███████║██║  ██║██║  ██║\n" +
            "    ╚═════╝╚══════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝\n" +
            "    ██████╗██╗██████╗ ██╗  ██╗███████╗██████╗\n" +
            "   ██╔════╝██║██╔══██╗██║  ██║██╔════╝██╔══██╗\n" +
            "   ██║     ██║██████╔╝███████║█████╗  ██████╔╝\n" +
            "   ██║     ██║██╔═══╝ ██╔══██║██╔══╝  ██╔══██╗\n" +
            "   ╚██████╗██║██║     ██║  ██║███████╗██║  ██║\n" +
            "    ╚═════╝╚═╝╚═╝     ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝\n")

        exit_program = 1
        choice = 9

        while choice != 0:

            print("\nWelcome to the Caesar Cipher Program\n")
            print("1. Encrypt")
            print("2. Decrypt")
            print("3. Brute force decrypt")
            print("0. Exit")

            choice = int(input("\nEnter your choice: "))

            if choice == 1:
                cls()
                text = input("Enter the text to encrypt: ")
                order = int(input("Enter the order: "))
                cipher = cp.Ceasar(text, order, 0)
                print("\nEncrypted text: ", cipher)

            elif choice == 2:
                cls()
                text = input("Enter the text to decrypt: ")
                order = int(input("Enter the order: "))
                cipher = cp.Ceasar(text, order, 1)
                print("\nDecrypted text: ", cipher)

            elif choice == 3:
                cls()
                text = input("Enter the text to decrypt: ")
                cls()
                for x in range(1, 27):
                    cipher = cp.Ceasar(text, x, 1)
                    print("Decrypted text: ", cipher)

            elif choice == 0:
                cls()
                print("\nThank you for using the cipher program")
                exit()

            else:
                cls()
                print("\nInvalid choice")

            print("\nDeseja continuar o programa? \n1. Sim \n0. Não")
            exit_program = int(input("\nEnter your choice: "))
            if exit_program == 0:
                cls()
                print("\nThank you for using the cipher program")
                exit()

            cls()

