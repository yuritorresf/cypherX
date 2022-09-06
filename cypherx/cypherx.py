#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import string

import time
import os
from rich import print
from rich.console import Console

import interface

class CypherX:

    def __init__(self, args):
        
        self.console = Console()
        
        print()

        if len(sys.argv) >= 1:
            
            self.__version__ = '1.3.1'

            if args.caesar:
                if args.key and args.message:
                    if args.encrypt:

                        with self.console.status("[bold green] Encrypting...[/bold green]",) as status:
                            caesar = Caesar(args.message, int(args.key), 0)
                            time.sleep(1)

                        if args.verbose:
                            cli = interface.CLI(caesar, args.message, args.key, "caesar", "verbose", "encrypt")
                        
                        elif args.quiet:
                            cli = interface.CLI(caesar, args.message, args.key, "caesar", "quiet", "encrypt")
                        
                        else:
                            cli = interface.CLI(caesar, args.message, args.key, "caesar", "normal", "encrypt")
                    
                        cli.banner()
                        cli.showResult()
                    
                    elif args.decrypt:

                        with self.console.status("[bold green] Decrypting...[/bold green]",) as status:
                            caesar = Caesar(args.message, int(args.key), 0)
                            time.sleep(1)

                        if args.verbose:
                            cli = interface.CLI(caesar, args.message, args.key, "caesar", "verbose", "decrypt")
                        
                        elif args.quiet:
                            cli = interface.CLI(caesar, args.message, args.key, "caesar", "quiet", "decrypt")
                        
                        else:
                            cli = interface.CLI(caesar, args.message, args.key, "caesar", "normal", "decrypt")
                    
                        cli.banner()
                        cli.showResult()

                    elif args.force_decrypt:

                        with self.console.status("[bold green] Force decrypting...[/bold green]",) as status:
                            caesar = Caesar(args.message, int(args.key), 2).force()
                            time.sleep(1)

                        if args.verbose:
                            cli = interface.CLI(caesar, args.message, args.key, 1, 1, 1)
                        
                        elif args.quiet:
                            cli = interface.CLI(caesar, args.message, args.key, 1, 2, 1)
                        
                        else:
                            cli = interface.CLI(caesar, args.message, args.key, 1, 0, 1)
                    
                        cli.banner()
                        cli.showResult()
                    else:
                        print("[!] Error: Missing key arguments.\nUse 'cypherx -h' for more information.")
                

                elif args.force_decrypt:
                    if args.message != None or args.message != "":
                        if args.verbose:
                            print(f"[bold gray]\nCypherX version {self.__version__}[/bold gray]. [bold red]Caesar[/bold red] cipher, [bold green]decrypt[/bold green] method in [bold yellow]verbose[/bold yellow] mode.\n")
                        elif args.quiet:
                            pass
                        else:
                            print(f"[bold gray]\nCypherX version {self.__version__}[/bold gray]. [bold red]Caesar[/bold red] cipher, [bold green]decrypt[/bold green] method in [bold yellow]normal[/bold yellow] mode.\n")
                            
                        with self.console.status("[bold green] Decrypting...[/bold green]",) as status:
                            caesar = Caesar(args.message, args.key, 2).force()
                            time.sleep(1)
                        
                        if args.verbose:
                            print(f"[bold][\N{check mark}] Message decrypted successfully![/bold]", end="\n", flush=True)
                            print(f"\n[gray][+] Message:[/gray] [bold yellow]{args.message}[/bold yellow]\n")
                            for d in caesar:
                                print(f"[gray][-] Decrypted message:[/gray] [bold green]{d}[/bold green]")
                            print(f"\n[gray][\N{check mark}][/gray][bold green] Done![/bold green]")
                        elif args.quiet:
                            print(caesar)
                        else:
                            print(f"[bold][\N{check mark}] Message encrypted successfully![/bold]", end="\n\n", flush=True)
                            for d in caesar:
                                print(f"[gray][-] Decrypted message:[/gray] [bold green]{d}[/bold green]")
                            print(f"\n[gray][\N{check mark}][/gray][bold green] Done![/bold green]")

                else:
                    print("[!] Error: You must choose between encrypt or decrypt.")
            elif args.atbash:

                if args.verbose:
                    print(f"[bold gray]\nCypherX version {self.__version__}[/bold gray]. [bold red]Atbash[/bold red] cipher, [bold green]encrypt[/bold green] method in [bold yellow]verbose[/bold yellow] mode.\n")
                elif args.quiet:
                    pass
                else:
                    print(f"[bold gray]\nCypherX version {self.__version__}[/bold gray]. [bold red]Atbash[/bold red] cipher, [bold green]encrypt[/bold green] method in [bold yellow]normal[/bold yellow] mode.\n")
                    
                if args.encrypt:  
                    with self.console.status("[bold green] Encrypting...[/bold green]",) as status:
                        atbash = Atbash(args.message, 0)
                        time.sleep(1)

                    if args.message:
                        if args.verbose:
                            print(f"[bold][\N{check mark}] Message encrypted successfully![/bold]", end="\n", flush=True)
                            print(f"\n[gray][+] Message:[/gray] [bold yellow]{args.message}[/bold yellow]")
                            print(f"[gray][=] Encrypted message:[/gray] [bold green]{atbash}[/bold green]")
                            print(f"\n[gray][\N{check mark}][/gray][bold green] Done![/bold green]")
                        elif args.quiet:
                            print(atbash)
                        else:
                            print(f"[bold][\N{check mark}] Message encrypted successfully![/bold]", end="\n\n", flush=True)
                            print(f"[gray][=] Encrypted message:[/gray] [bold green]{atbash}[/bold green]")
                            print(f"\n[gray][\N{check mark}][/gray][bold green] Done![/bold green]")

                elif args.decrypt:
                    with self.console.status("[bold green] Decrypting...[/bold green]",) as status:
                        atbash = Atbash(args.message, 1)
                        time.sleep(1)

                    if args.message:
                        if args.verbose:
                            print(f"[bold][\N{check mark}] Message decrypted successfully![/bold]", end="\n", flush=True)
                            print(f"\n[gray][+] Message:[/gray] [bold yellow]{args.message}[/bold yellow]")
                            print(f"[gray][=] Decrypted message:[/gray] [bold green]{atbash}[/bold green]")
                            print(f"\n[gray][\N{check mark}][/gray][bold green] Done![/bold green]")
                        elif args.quiet:
                            print(atbash)
                        else:
                            print(f"[bold][\N{check mark}] Message decrypted successfully![/bold]", end="\n\n", flush=True)
                            print(f"[gray][=] Decrypted message:[/gray] [bold green]{atbash}[/bold green]")
                            print(f"\n[gray][\N{check mark}][/gray][bold green] Done![/bold green]")
                else:
                    print("[!] Error: You must choose between encrypt or decrypt.")
            elif args.command == 'start':
                interface.StartTUI()
class Caesar:

    def __init__(self, text, order, mod):
        self.text, self.order, self.mod = text, order, mod
        self.order = order
        
        self.alphabet = string.ascii_lowercase
        self.alphabet_upper = string.ascii_uppercase

        if self.mod == 0:
            self.data = self.encrypt()
        elif self.mod == 1:
            self.data = self.decrypt()
        elif self.mod == 2:
            self.data = self.force()
        else:
            raise ValueError("Invalid mod")
    
    def encrypt(self):
        encrypted = ""
        for char in self.text:
            if char in self.alphabet:
                encrypted += self.alphabet[(self.alphabet.index(char) + self.order) % 26]
            elif char in self.alphabet_upper:
                encrypted += self.alphabet_upper[(self.alphabet_upper.index(char) + self.order) % 26]
            else:
                encrypted += char
        return encrypted
    
    def decrypt(self):
        decrypted = ""
        for char in self.text:
            if char in self.alphabet:
                decrypted += self.alphabet[(self.alphabet.index(char) - self.order) % 26]
            elif char in self.alphabet_upper:
                decrypted += self.alphabet_upper[(self.alphabet_upper.index(char) - self.order) % 26]
            else:
                decrypted += char
        return decrypted

    def force(self):
        forced_data = []
        for i in range(26):
            self.order = i
            forced_data.append(self.decrypt())

        return forced_data

    def __str__(self):
        return self.data

class Atbash:

    def __init__(self, text=str, mod=int) -> str:
        self.__text = text
        self.__mod = mod

        self.alphabet = string.ascii_lowercase
        self.alphabet_upper = string.ascii_uppercase

        if self.__mod == 0:
            self.data = self.encrypt()
        elif self.__mod == 1:
            self.data = self.decrypt()
        else:
            raise ValueError("[!] Invalid mod")

    def encrypt(self) -> str:
        encrypted = ""
        for char in self.__text:
            if char in self.alphabet:
                encrypted += self.alphabet[25 - self.alphabet.index(char)]
            elif char in self.alphabet_upper:
                encrypted += self.alphabet_upper[25 - self.alphabet_upper.index(char)]
            else:
                encrypted += char
        return encrypted

    def decrypt(self) -> str:
        decrypted = ""
        for char in self.__text:
            if char in self.alphabet:
                decrypted += self.alphabet[25 - self.alphabet.index(char)]
            elif char in self.alphabet_upper:
                decrypted += self.alphabet_upper[25 - self.alphabet_upper.index(char)]
            else:
                decrypted += char
        return decrypted
    
    def __str__(self) -> str:
        return self.data

