from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Inicializar o navegador
driver = webdriver.Chrome('C:\Users\user\Downloads\chrome-win64')  

# Abrir o WhatsApp Web
driver.get('https://web.whatsapp.com/')
input("Escaneie o QR Code e pressione Enter quando estiver logado no WhatsApp Web:")

# Definir o grupo e a mensagem específica para responder
grupo_nome = "Conteúdo Exclusivo"  # Insira o nome exato do grupo
mensagem_responder = "oi"

# Encontrar o grupo na lista de chats
grupo = driver.find_element_by_xpath(f"//span[@title='{grupo_nome}']")
grupo.click()

# Loop para verificar novas mensagens
while True:
    # Encontrar todas as mensagens no chat
    mensagens = driver.find_elements_by_xpath("//div[@class='copyable-text']")

    # Iterar sobre as mensagens
    for mensagem in mensagens:
        texto = mensagem.text
        if texto == mensagem_responder:
            # Enviar a resposta
            resposta = "Teste realizado com Sucesso!"
            caixa_mensagem = driver.find_element_by_xpath("//div[@contenteditable='true']")
            caixa_mensagem.send_keys(resposta + Keys.RETURN)
    
    # Esperar um pouco antes de verificar novamente
    time.sleep(2)

# Fechar o navegador
driver.quit()
