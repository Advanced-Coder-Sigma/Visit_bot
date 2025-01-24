from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
import requests

TOKEN = "7627406156:AAEnJDvSJrzNr9kY43sNzv6cYqoxMt9k-w0"
ALLOWED_GROUP_ID = -1002392794494
USER_VISIT_COUNT = {}

def add_visit(uid: int) -> str:
    url = f"https://freefire.scaninfo.net/visit/?uid={uid}"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return f"🎉✅Successfully sent 10000+ views to your UID {uid}✅🎉                                        ☆DM ME FOR PURCHASING API,SCRIPT & ACCESS-----@Bhaiya_chips"
        else:
            return f"🚫Error: Unable to add visits to UID {uid}🚫"
    except Exception as e:
        return f"Error: {str(e)}"

async def visit(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.chat_id != ALLOWED_GROUP_ID:
        await update.message.reply_text("This command can only be used in the allowed group.")
        return

    try:
        uid = int(context.args[0])
        user_id = update.message.from_user.id
        if user_id not in USER_VISIT_COUNT:
            USER_VISIT_COUNT[user_id] = 0
        
        if USER_VISIT_COUNT[user_id] >= 100:
            await update.message.reply_text("🔥You have reached the limit of 200 visits per day🔥")
            return

        message = await update.message.reply_text(f"Sending views to UID {uid}, please wait...")
        result = add_visit(uid)
        USER_VISIT_COUNT[user_id] += 1
        await message.delete()
        await update.message.reply_text(result, reply_to_message_id=update.message.message_id)
    except (IndexError, ValueError):
        await update.message.reply_text(
"❌Incorrect format! 🙏🏻Please use the command in the format: /visit {uid}"
 "Example : /visit 12345678"
        )

if __name__ == "__main__":
    application = Application.builder().token(TOKEN).build()
    application.add_handler(CommandHandler("visit", visit))
    application.run_polling()
