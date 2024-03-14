import logging
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
from googletrans import Translator

# Set up logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

class TranslationBot:
    def __init__(self, token):
        # Inisialisasi Updater dengan token bot
        self.updater = Updater(token, use_context=True)

        # Inisialisasi dispatcher
        self.dispatcher = self.updater.dispatcher

        # Inisialisasi Translator dari googletrans
        self.translator = Translator()

        # Menambahkan handler untuk perintah /start
        self.dispatcher.add_handler(CommandHandler("start", self.start))

        # Menambahkan handler untuk menerima pesan dan menerjemahkan
        self.dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, self.translate))

    def start(self, update: Update, context: CallbackContext) -> None:
        # Pesan selamat datang
        welcome_message = "Welcome! This bot will translate your messages to multiple languages."

        # Kirim pesan selamat datang
        update.message.reply_text(welcome_message)

    def translate(self, update: Update, context: CallbackContext) -> None:
        # Handle pesan teks yang dikirimkan
        message = update.message.text

        # Daftar bahasa tujuan yang ingin diterjemahkan
        target_languages = ['id', 'en', 'de', 'ko', 'fr', 'es', 'zh-CN', 'ru']
        translated_messages = []

        # Terjemahkan pesan ke masing-masing bahasa tujuan
        for lang in target_languages:
            translated_message = self.translate_message(message, lang)
            translated_messages.append(translated_message)

        # Kirim pesan hasil terjemahan ke pengguna
        reply_message = f"Translation Results:\n\nBahasa Indonesia: {translated_messages[0]}\n" \
                        f"English: {translated_messages[1]}\nDeutsch (German): {translated_messages[2]}\n" \
                        f"한국어 (Korea): {translated_messages[3]}\nFrançais: {translated_messages[4]}\n" \
                        f"Español: {translated_messages[5]}\n中文 (Mandarin): {translated_messages[6]}\n" \
                        f"Русский (Rusia): {translated_messages[7]}"
        update.message.reply_text(reply_message)

    def translate_message(self, message, dest_language='en') -> str:
        # Fungsi untuk menerjemahkan pesan
        translated = self.translator.translate(message, src='auto', dest=dest_language)
        return translated.text

    def start_polling(self):
        # Fungsi untuk memulai polling
        self.updater.start_polling()

    def idle(self):
        # Fungsi untuk menghentikan bot
        self.updater.idle()

def main():
    # Ganti dengan token bot Anda
    TOKEN = "7195094751:AAFkh-mVMycTMmq0dsI5U3NKYIE5Y96qT0Q"
    bot = TranslationBot(TOKEN)
    bot.start_polling()
    bot.idle()

if __name__ == "__main__":
    main()
