import os
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# Função para o comando /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Olá! Eu sou um bot de eco. Envie qualquer mensagem e eu a repetirei.')

# Função que repete a mensagem do usuário
async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(update.message.text)

def main():
    # Pega o token de uma variável de ambiente, é mais seguro e ideal para deploy
    TOKEN = os.environ.get('TELEGRAM_TOKEN')

    # Cria a aplicação do bot
    application = Application.builder().token(TOKEN).build()

    # Adiciona os "escutadores" de comandos e mensagens
    application.add_handler(CommandHandler('start', start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    # Inicia o bot
    application.run_polling()

if __name__ == '__main__':
    main()
