from colorama import Fore
class CustomMessage:

    def errorMessage(self, content):
        raise(f"{Fore.RED}{content}{Fore.RESET}")

    def successMessage(self, content):
        return print(f"{Fore.GREEN}{content}{Fore.RESET}")
