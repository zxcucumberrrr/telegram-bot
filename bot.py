from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("Товары", callback_data="products")],
        [
            InlineKeyboardButton("Поддержка", callback_data="support"),
            InlineKeyboardButton("Профиль", callback_data="profile")
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await context.bot.send_photo(
        chat_id=update.effective_chat.id,
        photo="https://i.postimg.cc/63tMMVn3/png-transparent-smiley-emoticon-animation-goodbye-miscellaneous-face-words-phrases-2.png",
        caption="👋 Добро пожаловать в Talan41k Store",
        reply_markup=reply_markup
    )

async def handle_button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == "profile":
        
        user_id = str(update.effective_user.id)
        context.user_data.setdefault("id", user_id)
        context.user_data.setdefault("topup_count", 0)
        context.user_data.setdefault("order_count", 0)
        context.user_data.setdefault("balance", 0)

        profile_caption = (
            f"Ваш ID профиля: `{context.user_data['id']}`\n"
            f"Количество пополнений: {context.user_data['topup_count']}\n"
            f"Количество заказов: {context.user_data['order_count']}\n\n"
            f"Баланс: {context.user_data['balance']}₽\n\n"
            f"Получайте приятные бонусы от покупок по вашей рефералке:\n"
            f"Ваша ссылка: https://t.me/talan41kvbot?start={context.user_data['id']}"
        )

        keyboard = [
            [InlineKeyboardButton("Пополнить баланс 💰", callback_data="topup")],
            [InlineKeyboardButton("Использовать промокод 🎁", callback_data="promo")]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)

        await context.bot.send_photo(
            chat_id=query.message.chat.id,
            photo="https://i.postimg.cc/gJ7NmC1w/photo-2025-08-03-04-04-15.jpg",
            caption=profile_caption,
            reply_markup=reply_markup,
            parse_mode="Markdown"
        )

    elif query.data == "products":
        await query.edit_message_text("🛒 Вот список товаров...")
    elif query.data == "support":
        await query.edit_message_text("📞 Поддержка: @eto_lesovichok")

import os
app = ApplicationBuilder().token(os.getenv("8370802531:AAFO_5qnac-rpXDRQf6-F8P6h4QCclmhHvM")).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CallbackQueryHandler(handle_button))
app.run_polling()
