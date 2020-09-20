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
driver = None

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
            clear()
            start_sending()
        elif choice == 2:
            clear()
            mng_contacts()
        elif choice == 3:
            clear()
            mng_attachments()
        elif choice == 4:
            clear()
            mng_message()
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
    print(f'{Fore.CYAN}3.{Style.RESET_ALL} Voltar\n')
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
    print(f'{Fore.CYAN}# Whatsapp Automation Tool')
    print(f'{Fore.CYAN}# Gerenciar anexos\n')
    print(f'{Fore.CYAN}1.{Style.RESET_ALL} Documentos')
    print(f'{Fore.CYAN}2.{Style.RESET_ALL} Imagens/Videos')
    print(f'{Fore.CYAN}3.{Style.RESET_ALL} Voltar\n')
    try:
        choice = int(input(f'{Style.RESET_ALL}Digite a opção desejada [1-3]:{Fore.CYAN} '))

        if choice == 1:
            clear()
            documents_menu()
        elif choice == 2:
            clear()
            media_menu()
        elif choice == 3:
            clear()
            main_menu()
        else:
            send_error('ERRO: Opção inválida!')
            mng_attachments()
    except ValueError:
        send_error('ERRO: Opção inválida!')
        mng_attachments()

def documents_menu():
    print(f'{Fore.CYAN}# Whatsapp Automation Tool')
    print(f'{Fore.CYAN}# Documentos')
    
    if len(documents) > 0:
        print(f'\n{Style.RESET_ALL}{documents}\n')
    else:
        print(f'\n{Fore.RED}# Você ainda não anexou documentos!\n')

    print(f'{Fore.CYAN}1.{Style.RESET_ALL} Anexar documento')
    print(f'{Fore.CYAN}2.{Style.RESET_ALL} Remover documento')
    print(f'{Fore.CYAN}3.{Style.RESET_ALL} Voltar\n')
    try:
        choice = int(input(f'{Style.RESET_ALL}Digite a opção desejada [1-3]:{Fore.CYAN} '))

        if choice == 1:
            clear()
            add_attachment(1)
        elif choice == 2:
            clear()
            rmv_attachment(1)
        elif choice == 3:
            clear()
            mng_attachments()
        else:
            send_error('ERRO: Opção inválida!')
            documents_menu()
    except ValueError:
        send_error('ERRO: Opção inválida!')
        documents_menu()

def media_menu():
    print(f'{Fore.CYAN}# Whatsapp Automation Tool')
    print(f'{Fore.CYAN}# Imagens/videos')
    
    if len(media) > 0:
        print(f'\n{Style.RESET_ALL}{media}\n')
    else:
        print(f'\n{Fore.RED}# Você ainda não anexou imagens/videos!\n')

    print(f'{Fore.CYAN}1.{Style.RESET_ALL} Anexar imagem/video')
    print(f'{Fore.CYAN}2.{Style.RESET_ALL} Remover imagem/video')
    print(f'{Fore.CYAN}3.{Style.RESET_ALL} Voltar\n')
    try:
        choice = int(input(f'{Style.RESET_ALL}Digite a opção desejada [1-3]:{Fore.CYAN} '))

        if choice == 1:
            clear()
            add_attachment(2)
        elif choice == 2:
            clear()
            rmv_attachment(2)
        elif choice == 3:
            clear()
            mng_attachments()
        else:
            send_error('ERRO: Opção inválida!')
            media_menu()
    except ValueError:
        send_error('ERRO: Opção inválida!')
        media_menu()

def add_attachment(type):
    if type == 1:
        global documents

        print(f'{Fore.CYAN}# Whatsapp Automation Tool')
        print(f'{Fore.CYAN}# Anexar documento\n')
        
        print(f"{Fore.YELLOW}# Digite 'Voltar' caso tenha desistido de anexar!")
        attach = str(input(f'{Fore.CYAN}#{Style.RESET_ALL} Digite o nome do documento que deseja anexar:{Fore.CYAN} '))
        
        if attach == 'Voltar' or attach == 'voltar':
            clear()
            documents_menu()
        else:
            file = f'{os.getcwd()}//documentos//{attach}'
            if os.path.exists(file):
                documents.append(attach)
                print(f'{Fore.GREEN}# O documento {attach} foi anexado!')
                input(f'{Style.RESET_ALL}\nPressione Enter para continuar...')
                clear()
                documents_menu()
            else:
                send_error('ERRO: Arquivo não encontrado na pasta documentos!')
                add_attachment(1)
    else:
        global media

        print(f'{Fore.CYAN}# Whatsapp Automation Tool')
        print(f'{Fore.CYAN}# Anexar imagem/video\n')
        
        print(f"{Fore.YELLOW}# Digite 'Voltar' caso tenha desistido de anexar!")
        attach = str(input(f'{Fore.CYAN}#{Style.RESET_ALL} Digite o nome do imagem/video que deseja anexar:{Fore.CYAN} '))
        
        if attach == 'Voltar' or attach == 'voltar':
            clear()
            media_menu()
        else:
            file = f'./midia/{attach}'
            if os.path.exists(file):
                media.append(attach)
                print(f'{Fore.GREEN}# A imagem/video {attach} foi anexada!')
                input(f'{Style.RESET_ALL}\nPressione Enter para continuar...')
                clear()
                media_menu()
            else:
                send_error('ERRO: Arquivo não encontrado na pasta midia!')
                add_attachment(2)

def rmv_attachment(type):
    if type == 1:
        global documents
        if len(documents) == 0 :
            send_error('ERRO: Você ainda não anexou documentos!')
            documents_menu()     
        print(f'{Fore.CYAN}# Whatsapp Automation Tool')
        print(f'{Fore.CYAN}# Remover documentos')
        print(f'\n{Style.RESET_ALL}{documents}\n')
        try:
            print(f"{Fore.YELLOW}# Digite 'Voltar' caso tenha desistido de remover um documento!")
            attach = str(input(f'{Fore.CYAN}#{Style.RESET_ALL} Digite o nome do documento que deseja remover:{Fore.CYAN} '))
            if attach == 'Voltar' or attach == 'voltar':
                clear()
                documents_menu()
            else:
                documents.remove(attach)
                print(f'{Fore.RED}# O documento {attach} foi removido!')
                input(f'\n{Style.RESET_ALL}Pressione Enter para continuar...')
                clear()
                documents_menu()
        except ValueError:
            send_error('ERRO: O documento desejado não está na lista!')
            rmv_attachment(1)
    else:
        global media
        if len(media) == 0 :
            send_error('ERRO: Você ainda não anexou imagens/videos!')
            media_menu()     
        print(f'{Fore.CYAN}# Whatsapp Automation Tool')
        print(f'{Fore.CYAN}# Remover imagens/videos')
        print(f'\n{Style.RESET_ALL}{media}\n')
        try:
            print(f"{Fore.YELLOW}# Digite 'Voltar' caso tenha desistido de remover uma imagem/video!")
            attach = str(input(f'{Fore.CYAN}#{Style.RESET_ALL} Digite o nome da imagem/video que deseja remover:{Fore.CYAN} '))
            if attach == 'Voltar' or attach == 'voltar':
                clear()
                media_menu()
            else:
                media.remove(attach)
                print(f'{Fore.RED}# A imagem/video {attach} foi removida!')
                input(f'\n{Style.RESET_ALL}Pressione Enter para continuar...')
                clear()
                media_menu()
        except ValueError:
            send_error('ERRO: A imagem/video desejado não está na lista!')
            rmv_attachment(2)

# ---
# Manage message
# ---
def mng_message():
    print(f'{Fore.CYAN}# Whatsapp Automation Tool')
    print(f'{Fore.CYAN}# Gerenciar mensagem')
    
    if len(message) > 0:
        print(f'\n{Style.RESET_ALL}{message}\n')
        print(f'{Fore.CYAN}1.{Style.RESET_ALL} Alterar mensagem')
    else:
        print(f'\n{Fore.RED}# Você ainda não adicionou uma mensagem!\n')
        print(f'{Fore.CYAN}1.{Style.RESET_ALL} Adicionar mensagem')

    print(f'{Fore.CYAN}2.{Style.RESET_ALL} Remover mensagem')
    print(f'{Fore.CYAN}3.{Style.RESET_ALL} Voltar\n')
    try:
        choice = int(input(f'{Style.RESET_ALL}Digite a opção desejada [1-3]:{Fore.CYAN} '))

        if choice == 1:
            clear()
            add_message()
        elif choice == 2:
            clear()
            rmv_message()
        elif choice == 3:
            clear()
            main_menu()
        else:
            send_error('ERRO: Opção inválida!')
            mng_message()
    except ValueError:
        send_error('ERRO: Opção inválida!')
        mng_message()

def add_message():
    global message
    print(f'{Fore.CYAN}# Whatsapp Automation Tool')
    print(f'{Fore.CYAN}# Adicionar mensagem\n')
    print(f'{Fore.YELLOW}# Digite sua mensagem e adicione um "~" ao finalizar a mensagem.')
    print(f'{Fore.YELLOW}# Ex: Olá, essa é uma mensagem de exemplo!~\n{Style.RESET_ALL}')
    message = []
    temp = ""
    done = False
    while done == False:
        temp = input()
        if len(temp) != 0 and temp[-1] == "~":
            done = True
            message.append(temp[:-1])
        else:
            message.append(temp)          
    message = "\n".join(message)
    input(f'{Style.RESET_ALL}\nPressione Enter para continuar...')
    clear()
    mng_message()

def rmv_message():
    global message
    print(f'{Fore.CYAN}# Whatsapp Automation Tool')
    print(f'{Fore.CYAN}# Remover mensagem\n')
    print(f'{Fore.CYAN}1.{Style.RESET_ALL} Sim')
    print(f'{Fore.CYAN}2.{Style.RESET_ALL} Não\n')
    try:
        choice = int(input(f'{Style.RESET_ALL}Digite a opção desejada [1-2]:{Fore.CYAN} '))

        if choice == 1:
            clear()
            print(f'{Fore.CYAN}# Whatsapp Automation Tool')
            print(f'{Fore.CYAN}# Remover mensagem\n')
            message = []
            print(f'{Fore.RED}# Mensagem excluída com sucesso!')
            input(f'{Style.RESET_ALL}\nPressione Enter para continuar...')
            clear()
            mng_message()
        elif choice == 2:
            clear()
            mng_message()
        else:
            send_error('ERRO: Opção inválida!')
            rmv_message()
    except ValueError:
        send_error('ERRO: Opção inválida!')
        mng_message()      

# ---
# Execute
# ---
def start_sending():
    global contacts, numbers
    
    if len(contacts) == 0 and len(numbers) == 0:
        send_error('ERRO: Você ainda não adicionou nenhum contato!')
        main_menu()  
    
    if len(message) == 0 and len(documents) == 0 and len(media) == 0:
        send_error('ERRO: Você ainda não adicionou nenhuma mensagem ou anexo!')
        main_menu() 

    print(f'{Fore.YELLOW}\n# ATENÇÃO!')
    print(f'{Fore.YELLOW}# Antes de continuar verifique se o WhatsApp está conectado!')
    print(f'{Fore.YELLOW}# Caso não esteja, escaneie o QR CODE da página antes de continuar!')
    input(f'{Style.RESET_ALL}\n# Pressione Enter para continuar...')
    
    clear()
    if len(contacts) > 0:
       for i in contacts:
            print(f'{Fore.YELLOW}\n# Enviando mensagem para {i}')
            send_message(1, i)
            sleep(1)
    if len(numbers) > 0:
        for i in numbers:
            link = f'https://web.whatsapp.com/send?phone={i}'
            driver.get(link)
            print(f'{Fore.YELLOW}\n# Enviando mensagem para {i}')
            send_message(2, i)
            sleep(1)
    print(f'{Fore.GREEN}\n# FIM DA TAREFA!')
    input(f'{Style.RESET_ALL}\nPressione Enter para continuar...')
    driver.close()
    os._exit(0)

# ---
# Send messages
# ---
def send_message(type, receiver):
    if type == 1:
        try:
            search_box=wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="side"]/div[1]/div/label/div/div[2]')))
            search_box.click()
            search_box.send_keys(receiver)

            rc = '"' + receiver + '"'
            x_arg = '//span[contains(@title,' + rc + ')]'
            contact_tile = wait.until(EC.presence_of_element_located((By.XPATH, x_arg)))
            contact_tile.click() 

            input_box = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')))
            for ch in message:       
                if ch == "\n":
                    ActionChains(driver).key_down(Keys.SHIFT).key_down(Keys.ENTER).key_up(Keys.ENTER).key_up(Keys.SHIFT).key_up(Keys.BACKSPACE).perform()
                else:
                    input_box.send_keys(ch)
            input_box.send_keys(Keys.ENTER)
            print(f'{Fore.GREEN}# Mensagem enviada para {receiver}')
            #send_attachment(receiver)
        except NoSuchElementException:
            print(f'{Fore.RED}# Falha ao enviar mensagem para {receiver}')
    else:
        try:
            # Espera até o avatar do usuário ser exibido.
            # O avatar do usuário é carregado junto com a página.
            # Assim é possível verificar se a página foi completamente carregada.
            # Para evitar erros de elementos não encotnrados.
            wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="side"]/header/div[1]/div/img')))
            sleep(1)

            # Verifica se a caixa de mensagem apareceu
            # Caso sim, continua o envio da mensagem normalmente.
            # Caso não, ele retornar um erro, pois o número não existe.
            input_box = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
            for ch in message:       
                if ch == "\n":
                    ActionChains(driver).key_down(Keys.SHIFT).key_down(Keys.ENTER).key_up(Keys.ENTER).key_up(Keys.SHIFT).key_up(Keys.BACKSPACE).perform()
                else:
                    input_box.send_keys(ch)
            input_box.send_keys(Keys.ENTER)
            print(f'{Fore.GREEN}# Mensagem enviada para {receiver}')
            send_attachment(receiver)   
        except NoSuchElementException:
            print(f'{Fore.RED}# Falha ao enviar mensagem para {receiver}')

# ---
# Send attachments
# ---
def send_attachment(receiver):
   if len(documents) > 0:
        for i in documents:
            attachment_path = f'{os.getcwd()}//documentos//{i}'
            print(f'{Fore.YELLOW}# Enviando o documento {i} para {receiver}')
            try:
                attachment_button = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="main"]/footer/div[1]/div[1]/div[2]/div')))
                attachment_button.click()
                
                document_input = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[1]/div[2]/span/div/div/ul/li[3]/button/input') 
                document_input.send_keys(attachment_path) 
                
                sleep(1)

                send_attachment_button = driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[2]/span/div/span/div/div/div[2]/span/div/div')
                send_attachment_button.click()
                print(f'{Fore.GREEN}# Documento {i} enviado para {receiver}')
            except NoSuchElementException:
                print(f'{Fore.RED}# Falha ao enviar o documento {i} para {receiver}')
            except FileNotFoundError:
                print(f'{Fore.RED}# Falha ao enviar o documento {i} para {receiver}')
        
        if len(documents) > 0:
            for i in media:
                attachment_path = f'{os.getcwd()}//midia//{i}'
                print(f'{Fore.YELLOW}# Enviando a imagem/video {i} para {receiver}')
                try:
                    attachment_button = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="main"]/footer/div[1]/div[1]/div[2]/div')))
                    attachment_button.click()
                    
                    media_input = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[1]/div[2]/span/div/div/ul/li[1]/button/input') 
                    media_input.send_keys(attachment_path) 
                    
                    sleep(1)

                    send_attachment_button = driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[2]/span/div/span/div/div/div[2]/span/div/div')
                    send_attachment_button.click()
                    print(f'{Fore.GREEN}# Imagem/video {i} enviada para {receiver}')
                except NoSuchElementException:
                    print(f'{Fore.RED}# Falha ao enviar a imagem/video {i} para {receiver}')
                except FileNotFoundError:
                    print(f'{Fore.RED}# Falha ao enviar a imagem/video {i} para {receiver}')

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
    args = Options()
    args.add_experimental_option('excludeSwitches', ['enable-logging']) 
    args.add_argument(r'--user-data-dir=./chrome_data')
    args.add_argument(r'--profile-directory=Default')
    args.binary_location = "C:/Program Files/Google/Chrome/Application/chrome.exe"

    driver = webdriver.Chrome(options=args, executable_path=r"./chromedriver")
    wait = WebDriverWait(driver, 600)
    driver.get('https://web.whatsapp.com')

    clear()
    main_menu()