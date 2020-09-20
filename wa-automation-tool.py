from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from time import sleep
from colorama import Fore
from colorama import Style
import os
import csv

# ---
# Global variables
# ---
contacts = []
numbers = []
message = []
media = []
documents = []

# ---
# Main menu
# ---
def main_menu():
    print(f'{Fore.CYAN}# Whatsapp Automation Tool')
    print(f'{Fore.CYAN}# Menu principal\n')
    print(f'{Fore.CYAN}1.{Style.RESET_ALL} Iniciar envio')
    print(f'{Fore.CYAN}2.{Style.RESET_ALL} Gerenciar contatos')
    print(f'{Fore.CYAN}3.{Style.RESET_ALL} Gerenciar anexos')
    print(f'{Fore.CYAN}4.{Style.RESET_ALL} Gerenciar mensagem')
    print(f'{Fore.CYAN}5.{Style.RESET_ALL} Sair\n')
    try:
        choice = int(input(f'{Style.RESET_ALL}Digite a opção desejada [1-5]:{Fore.CYAN} '))

        if choice == 1:
            pass
        elif choice == 2:
            clear()
            mng_contacts()
        elif choice == 3:
            pass
        elif choice == 4:
            pass
        elif choice == 5:
            pass
        else:
            send_error('ERRO: Opção inválida!')
            main_menu()
    except ValueError:
        send_error('ERRO: Opção inválida!')
        main_menu()

# ---
# Manage contacts
# ---
def mng_contacts():
    print(f'{Fore.CYAN}# Whatsapp Automation Tool')
    print(f'{Fore.CYAN}# Gerenciar contatos\n')
    print(f'{Fore.CYAN}1.{Style.RESET_ALL} Contatos')
    print(f'{Fore.CYAN}2.{Style.RESET_ALL} Números')
    print(f'{Fore.CYAN}3.{Style.RESET_ALL} Voltark\n')
    try:
        choice = int(input(f'{Style.RESET_ALL}Digite a opção desejada [1-3]:{Fore.CYAN} '))

        if choice == 1:
            clear()
            contacts_menu()
        elif choice == 2:
            clear()
            numbers_menu()
        elif choice == 3:
            clear()
            main_menu()
        else:
            send_error('ERRO: Opção inválida!')
            mng_contacts()
    except ValueError:
        send_error('ERRO: Opção inválida!')
        mng_contacts()

def contacts_menu():
    print(f'{Fore.CYAN}# Whatsapp Automation Tool')
    print(f'{Fore.CYAN}# Contatos')

    if len(contacts) > 0:
        print(f'\n{Style.RESET_ALL}{contacts}\n')
    else:
        print(f'\n{Fore.RED}# Você ainda não adicionou contatos a lista!\n')

    print(f'{Fore.CYAN}1.{Style.RESET_ALL} Adicionar contatos')
    print(f'{Fore.CYAN}2.{Style.RESET_ALL} Remover contato')
    print(f'{Fore.CYAN}3.{Style.RESET_ALL} Importar lista de contatos')
    print(f'{Fore.CYAN}4.{Style.RESET_ALL} Exportar lista de contatos')
    print(f'{Fore.CYAN}5.{Style.RESET_ALL} Voltar\n')
    try:
        choice = int(input(f'{Style.RESET_ALL}Digite a opção desejada [1-5]:{Fore.CYAN} '))

        if choice == 1:
            clear()
            add_contacts(1)
        elif choice == 2:
            clear()
            rmv_contacts(1)
        elif choice == 3:
            clear()
            import_contacts(1)
        elif choice == 4:
            clear()
            export_contacts(1)
        elif choice == 5:
            clear()
            mng_contacts()
        else:
            send_error('ERRO: Opção inválida!')
            contacts_menu()
    except ValueError:
        send_error('ERRO: Opção inválida!')
        contacts_menu()

def numbers_menu():
    print(f'{Fore.CYAN}# Whatsapp Automation Tool')
    print(f'{Fore.CYAN}# Números')

    if len(numbers) > 0:
        print(f'\n{Style.RESET_ALL}{numbers}\n')
    else:
        print(f'\n{Fore.RED}# Você ainda não adicionou números a lista!\n')

    print(f'{Fore.CYAN}1.{Style.RESET_ALL} Adicionar números')
    print(f'{Fore.CYAN}2.{Style.RESET_ALL} Remover número')
    print(f'{Fore.CYAN}3.{Style.RESET_ALL} Importar lista de números')
    print(f'{Fore.CYAN}4.{Style.RESET_ALL} Exportar lista de números')
    print(f'{Fore.CYAN}5.{Style.RESET_ALL} Voltar\n')
    try:
        choice = int(input(f'{Style.RESET_ALL}Digite a opcão desejada [1-5]:{Fore.CYAN} '))

        if choice == 1:
            clear()
            add_contacts(2)
        elif choice == 2:
            clear()
            rmv_contacts(2)
        elif choice == 3:
            clear()
            import_contacts(2)
        elif choice == 4:
            clear()
            export_contacts(2)
        elif choice == 5:
            clear()
            mng_contacts()
        else:
            send_error('ERRO: Opção inválida!')
            numbers_menu()
    except ValueError:
        send_error('ERRO: Opção inválida!')
        numbers_menu()

def add_contacts(type):
    if type == 1:
        global contacts
        print(f'{Fore.CYAN}# Whatsapp Automation Tool')
        print(f'{Fore.CYAN}# Adicionar contatos\n')

        try:
            print(f'{Fore.YELLOW}# Máximo de 20 contatos por vez.')
            print(f'{Fore.YELLOW}# Se quiser adicionar mais de 20 contatos, importe um arquivo .csv!\n')
            quantity = int(input(f'{Fore.CYAN}#{Style.RESET_ALL} Digite a quantidade que deseja adicionar:{Fore.CYAN} '))
            if quantity > 20:
                send_error('ERRO: Máximo de 20 contatos por vez!')
                add_contacts(1)
        except ValueError:
            send_error('ERRO: Use apenas números!')
            add_contacts(1)
            
        clear()
        print(f'{Fore.CYAN}# Whatsapp Automation Tool')
        print(f'{Fore.CYAN}# Adicionar contatos\n')

        for x in range(0, quantity):
            contact = str(input(f'{Fore.CYAN}#{Style.RESET_ALL} Digite o nome do contato {x+1}/{quantity}:{Fore.CYAN} '))
            contacts.append(contact)
        
        input(Style.RESET_ALL + '\nPressione Enter para continuar...')
        clear()
        contacts_menu()
    else:
        global numbers

        print(f'{Fore.CYAN}# Whatsapp Automation Tool')
        print(f'{Fore.CYAN}# Adicionar números\n')

        try:
            print(f'{Fore.YELLOW}# Máximo de 20 números por vez.')
            print(f'{Fore.YELLOW}# Se quiser adicionar mais de 20 números, importe um arquivo .csv!\n')
            quantity = int(input(f'{Fore.CYAN}#{Style.RESET_ALL} Digite a quantidade que deseja adicionar:{Fore.CYAN} '))
            if quantity > 20:
                send_error('ERRO: Máximo de 20 números por vez!')
                add_contacts(1)
        except ValueError:
            send_error('ERRO: Use apenas números!')
            add_contacts(1)
            
        clear()
        print(f'{Fore.CYAN}# Whatsapp Automation Tool')
        print(f'{Fore.CYAN}# Adicionar números\n')

        for x in range(0, quantity):
            try:
                number = int(input(f'{Fore.CYAN}#{Style.RESET_ALL} Digite o número de celular {x+1}/{quantity}:{Fore.CYAN} '))
                numbers.append(number)
            except ValueError:
                print(f'{Fore.RED}ERRO: Use apenas números, sem pontos ou hífens!')
                number = int(input(f'{Fore.CYAN}#{Style.RESET_ALL} Digite o número de celular {x+1}/{quantity}:{Fore.CYAN} '))
                numbers.append(number)
        
        input(Style.RESET_ALL + '\nPressione Enter para continuar...')
        clear()
        numbers_menu()

def rmv_contacts(type):
    if type == 1:
        global contacts
    
        if len(contacts) == 0:
            send_error('ERRO: Você ainda não adicionou nenhum contato!')
            contacts_menu()
            
        print(f'{Fore.CYAN}# Whatsapp Automation Tool')
        print(f'{Fore.CYAN}# Remover contatos')
        print(f'\n{Style.RESET_ALL}{contacts}\n')
        print(f"{Fore.YELLOW}# Digite 'Remover Todos' caso queira remover todos os contatos!")
        print(f"{Fore.YELLOW}# Digite 'Voltar' caso tenha desistido de remover!\n")
        try:
            contact = str(input(f'{Fore.CYAN}#{Style.RESET_ALL} Digite o contato que deseja remover:{Fore.CYAN} '))
            if contact == 'Remover Todos' or contact == 'remover todos':
                contacts = []
                print(f'{Fore.RED}# Todos os contatos foram removidos!')
            elif contact == 'Voltar' or contact == 'voltar':
                clear()
                contacts_menu()   
            else:
                contacts.remove(contact)
                print(f'{Fore.RED}# O contato {contact} foi removido!')
        
            input(f'{Style.RESET_ALL}\nPressione Enter para continuar...')
            clear()
            contacts_menu()
        except ValueError:
            send_error('ERRO: O contato digitado não está na lista!')
            rmv_contacts(1)
    else:
        global numbers
    
        if len(numbers) == 0:
            send_error('ERRO: Você ainda não adicionou nenhum número!')
            numbers_menu()
            
        print(f'{Fore.CYAN}# Whatsapp Automation Tool')
        print(f'{Fore.CYAN}# Remover números')
        print(f'\n{Style.RESET_ALL}{numbers}\n')
        print(f"{Fore.YELLOW}# Digite 'Remover Todos' caso queira remover todos os números!")
        print(f"{Fore.YELLOW}# Digite 'Voltar' caso tenha desistido de remover!\n")
        try:
            number = str(input(f'{Fore.CYAN}#{Style.RESET_ALL} Digite o número que deseja remover:{Fore.CYAN} '))
            if number == 'Remover Todos' or number == 'remover todos':
                numbers = []
                print(f'{Fore.RED}# Todos os números foram removidos!')
            elif number == 'Voltar' or number == 'voltar':
                clear()
                numbers_menu()   
            else:
                try:
                    numbers.remove(int(number))
                    print(f'{Fore.RED}# O número {number} foi removido!')
                except ValueError:
                    send_error('ERRO: O número digitado não está na lista!')
                    rmv_contacts(2)
            input(f'{Style.RESET_ALL}\nPressione Enter para continuar...')
            clear()
            numbers_menu()
        except ValueError:
            send_error('ERRO: O número digitado não está na lista!')
            rmv_contacts(2)

def import_contacts(type):
    if type == 1:
        global contacts
        print(f'{Fore.CYAN}# Whatsapp Automation Tool')
        print(f'{Fore.CYAN}# Importar contatos\n')
        try:
            with open('contatos.csv') as f:
                for row in f:
                    contacts.append(row.replace('\n',''))
            print(f'{Fore.GREEN}# Contatos importados com sucesso!')
            input(f'{Style.RESET_ALL}\nPressione Enter para continuar...')
            clear()
            contacts_menu()
        except FileNotFoundError:
            send_error('ERRO: O arquivo "contatos.csv" não foi encontrado!')
            contacts_menu()
    else:
        global numbers
        print(f'{Fore.CYAN}# Whatsapp Automation Tool')
        print(f'{Fore.CYAN}# Importar números\n')
        try:
            with open('numeros.csv') as f:
                for row in f:
                    numbers.append(row.replace('\n',''))
            print(f'{Fore.GREEN}# Números importados com sucesso!')
            input(f'{Style.RESET_ALL}\nPressione Enter para continuar...')
            clear()
            numbers_menu()
        except FileNotFoundError:
            send_error('ERRO: O arquivo "numeros.csv" não foi encontrado!')
            numbers_menu()

def export_contacts(type):
    if type == 1:
        global contacts

        if len(contacts) == 0:
            send_error('ERRO: Você ainda não adicionou nenhum contato!')
            contacts_menu()

        print(f'{Fore.CYAN}# Whatsapp Automation Tool')
        print(f'{Fore.CYAN}# Exportar contatos\n')  
        
        with open('contatos.csv', 'w', newline='') as f:
            wt = csv.writer(f)
            for i in contacts:
                wt.writerow([i])

        print(f'{Fore.GREEN}# Contatos exportados com sucesso!')
        input(f'{Style.RESET_ALL}\nPressione Enter para continuar...')
        clear()
        contacts_menu()
    else:
        global numbers

        if len(numbers) == 0:
            send_error('ERRO: Você ainda não adicionou nenhum número!')
            contacts_menu()

        print(f'{Fore.CYAN}# Whatsapp Automation Tool')
        print(f'{Fore.CYAN}# Exportar números\n')  

        with open('numeros.csv', 'w', newline='') as f:
            wt = csv.writer(f)
            for i in numbers:
                wt.writerow([i])

        print(f'{Fore.GREEN}# Números exportados com sucesso!')
        input(f'{Style.RESET_ALL}\nPressione Enter para continuar...')
        clear()
        numbers_menu()

# ---
# Manage attachments
# ---
def mng_attachments():
    pass

def add_attachment():
    pass

def rmv_attachment():
    pass

# ---
# Manage message
# ---
def mng_message():
    pass

def add_message():
    pass

def rmv_message():
    pass

# ---
# Execute
# ---
def execute():
    pass

# ---
# Send messages
# ---
def send_message():
    pass

# ---
# Send attachments
# ---
def send_attachment():
    pass

# ---
# Utility
# ---
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def send_error(error):
    clear()
    print(f'{Fore.RED}{error}')

# ---
# Main routine
# ---
if __name__ == "__main__":
    clear()
    main_menu()