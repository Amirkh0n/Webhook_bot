from django.http import JsonResponse
from telegram import Update
from telegram.ext import Dispatcher
from django.views.decorators.csrf import csrf_exempt
import json

# Telegram botni ulash
from telegram import Bot
TOKEN = 'YOUR_BOT_TOKEN'  # O'zingizning bot tokeningizni qo'ying
bot = Bot(token=TOKEN)

# Dispatcher ni sozlash
dispatcher = Dispatcher(bot, None, workers=0)

# CSRF ni chetlab o'tish kerak
@csrf_exempt
def webhook(request):
    if request.method == "POST":
        # JSON ma'lumotni o'qiymiz
        update = Update.de_json(json.loads(request.body), bot)
        dispatcher.process_update(update)
        return JsonResponse({"status": "ok"})
    return JsonResponse({"status": "not allowed"})


from telegram.ext import CommandHandler

# Bu /start buyrug'ini qayta ishlovchi funksiya
def start(update, context):
    update.message.reply_text('Assalomu alaykum! Bu bot ishga tushdi.')

# Bu yerda dispatcher'ga handler qo'shamiz
dispatcher.add_handler(CommandHandler('start', start))

