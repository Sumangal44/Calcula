import time
import os
import platform
from termcolor import colored

def clear_screen():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")

def display_banner():
    banner = r"""
  
  ___                                                     _ 
 / _ \                                                   | |
/ /_\ \_      _____  ___  ___  _ __ ___   ___    ___ __ _| |
|  _  \ \ /\ / / _ \/ __|/ _ \| '_ ` _ \ / _ \  / __/ _` | |
| | | |\ V  V /  __/\__ \ (_) | | | | | |  __/ | (_| (_| | |
\_| |_/ \_/\_/ \___||___/\___/|_| |_| |_|\___|  \___\__,_|_|
                                                            
                                                            


    """
    print(colored(banner, "cyan"))

def starting_animation():
    print(colored("Initializing...", "green"))
    time.sleep(1)
    print(colored("Loading...", "yellow"))
    time.sleep(1)
    print(colored("Ready!", "magenta"))
    time.sleep(1)

def calculator():
    print("Welcome to the Awesome Calculator!")
    print("Enter 'exit' to quit.")
    while True:
        expression = input("Enter your expression: ")
        if expression.lower() == "exit":
            break
        try:
            result = eval(expression)
            print(colored(f"Result: {result}", "cyan"))
        except Exception as e:
            print(colored(f"Error: {e}", "red"))

if __name__ == "__main__":
    clear_screen()
    display_banner()
    starting_animation()
    calculator()
