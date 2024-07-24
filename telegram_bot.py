import telebot

token = '5899828491:AAHHRWRnj7uP4ubWIbOiD7h1goj_jzOLO2g'
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def say_hello(message):
    responder()
    chat_id = message.chat.id
    bot.send_message(chat_id, "Olá, eu sou o DMC Bot!")

@bot.message_handler(commands=["opcao1"])
def opcao1(mensagem):
    texto = """
    O que você quer? (Clique em uma opção)
    /Log de Erro
    /Reload
    /nada"""
    bot.send_message(mensagem.chat.id, texto)
    
def verificar(mensagem):
    return True

@bot.message_handler(func=verificar)
def responder(mensagem):
    texto = """
    Escolha uma opção para continuar (Clique no item):
     /opcao1 Elib Aplicativo
     /opcao2 DMC Protocolos
     /opcao3 DMC Intranet
    Responder qualquer outra coisa não vai funcionar, clique em uma das opções"""
    bot.reply_to(mensagem, texto)
    
    
bot.polling()

## Academy Nupen 

## publister blogger template
## gnews blogger template
## melina blogger template
## 