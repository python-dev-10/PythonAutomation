from colorama import Fore
class CustomMessage:

    def error_message(self, content):
        return print(f"{Fore.RED}{content}{Fore.RESET}")

    def success_message(self, content):
        return print(f"{Fore.GREEN}{content}{Fore.RESET}")
