from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes

import os

TOKEN = os.getenv("BOT_TOKEN")

# --- MAIN PAGE ---
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = (
        "👋 WELCOME TO DIGI-BRIDGE!\n\n"
        "🌉 YOUR BRIDGE TO ACADEMIC SUCCESS 🚀\n\n"
        "🎓 LEARN FROM REAL SUCCESS\n"
        "Led by last year's Straight-A+ Achiever — a Software Engineering student "
        "who earned a GPA=4.0 (All A+) across his freshman courses.\n\n"
        "💡 WHAT YOU'LL GET\n"
        "☑️ Proven study strategies\n"
        "☑️ Exam preparation methods\n"
        "☑️ Direct academic advice\n"
        "☑️ Practical tips and tricks\n"
        "☑️ Step-by-step preparation guidance\n"
        "☑️ Organized learning and practice resources\n"
        "☑️ Guidance toward your desired academic program\n\n"
        "💎 PREMIUM ACCESS — ONLY 250 BIRR\n\n"
        "🏦 CBE\nAccount: 1000510260752\nName: Chala Merga Beyene\n\n"
        "📱 Telebirr\nPhone: 0965080186\nName: Aberash Merga\n\n"
        "🏦 Bankii Hojii Gamtaa Oromiyaa\nAccount: 1030700179656\nName: Chala Merga Beyene\n\n"
        "For other payment methods, contact @digibridge1.\n\n"
        "🚀 How to Join Premium\n"
        "1. Pay 250 Birr.\n"
        "2. Send your payment screenshot + your name to @digibridge1.\n"
        "3. Admin verifies your payment.\n"
        "4. You’ll be added to the private Digi-Bridge group.\n\n"
        "🎁 SPECIAL OFFER\nInvite 3 students who join Premium and get FREE access.\n\n"
        "👇 READY TO START?\nChoose an option below 👇"
    )

    # Copy buttons
    copy_buttons = [
        [InlineKeyboardButton("📋 Copy CBE Account", callback_data="copy_cbe")],
        [InlineKeyboardButton("📋 Copy Telebirr Phone", callback_data="copy_telebirr")],
        [InlineKeyboardButton("📋 Copy BOA Account", callback_data="copy_boa")]
    ]

    # Navigation buttons (2x2 grid)
    nav_buttons = [
        [InlineKeyboardButton("🌉 About Us", callback_data="about"),
         InlineKeyboardButton("📚 What Is Available?", callback_data="available")],
        [InlineKeyboardButton("📢 Join Digi-Bridge", callback_data="join"),
         InlineKeyboardButton("❓ Help", callback_data="help")]
    ]

    keyboard = copy_buttons + nav_buttons

    if update.message:
        await update.message.reply_text(
            text,
            reply_markup=InlineKeyboardMarkup(keyboard)
        )
    elif update.callback_query:
        query = update.callback_query
        await query.answer()
        await query.edit_message_text(
            text,
            reply_markup=InlineKeyboardMarkup(keyboard)
        )
# --- ABOUT US ---
async def about(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    text = (
        "🌉 ABOUT DIGI-BRIDGE\n\n"
        "Digi-Bridge is a student-focused academic support platform created to make freshman preparation more "
        "organized, practical, accessible, and effective.\n\n"
        "🎓 PROVEN BY REAL EXPERIENCE\n"
        "Built from the success of a 4.0 GPA achiever.\n\n"
        "🚀 OUR MISSION\n"
        "📚 Access quality academic resources\n"
        "🎯 Prepare strategically\n"
        "💡 Learn from proven experiences\n"
        "🤝 Receive mentorship\n"
        "🏆 Improve performance\n"
        "🚀 Build a stronger path toward your academic program\n\n"
        "🌉 Digi-Bridge — Your Bridge to Academic Success."
    )
    keyboard = [[InlineKeyboardButton("⬅️ Back to Main Menu", callback_data="main")]]
    await query.edit_message_text(text, reply_markup=InlineKeyboardMarkup(keyboard))

# --- WHAT IS AVAILABLE ---
async def available(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    text = (
        "📚 WHAT YOU GET ON DIGI-BRIDGE\n\n"
        "📖 ORGANIZED LEARNING MATERIALS\n☑️ Notes & Questions\n☑️ Video Tutorials\n\n"
        "📄 SOLVED EXAM PAPERS\n☑️ Mid Exams\n☑️ Final Exams\n☑️ COC Exams\n\n"
        "💻 ONLINE EXAMS & QUIZZES\n☑️ Unit Exams\n☑️ Topic Quizzes\n\n"
        "📝 MOCK EXAMS\n☑️ Mid Exam mocks\n☑️ Final Exam mocks\n☑️ COC Exam mocks\n\n"
        "🤝 SUPPORT\n☑️ Guidance from a 4.0 GPA achiever\n☑️ Mentorship\n☑️ Study tips\n\n"
        "🎯 Designed to help you learn, practice, prepare, and perform better."
    )
    keyboard = [[InlineKeyboardButton("⬅️ Back to Main Menu", callback_data="main")]]
    await query.edit_message_text(text, reply_markup=InlineKeyboardMarkup(keyboard))

# --- JOIN DIGI-BRIDGE ---
async def join(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    text = (
        "🚀 JOIN DIGI-BRIDGE PREMIUM\n\n"
        "Premium Access is only 250 Birr.\n\n"
        "💰 PAYMENT OPTIONS\n\n"
        "🏦 CBE\nAccount: 1000510260752\nName: Chala Merga Beyene\n\n"
        "📱 Telebirr\nPhone: 0965080186\nName: Aberash Merga\n\n"
        "🏦 Bankii Hojii Gamtaa Oromiyaa\nAccount: 1030700179656\nName: Chala Merga Beyene\n\n"
        "📩 AFTER PAYMENT\n1️⃣ Screenshot your payment\n2️⃣ Send to @digibridge1\n3️⃣ Admin verifies\n4️⃣ Access granted\n\n"
        "🎁 Invite 3 students and get Premium FREE!"
    )
    keyboard = [[InlineKeyboardButton("⬅️ Back to Main Menu", callback_data="main")]]
    await query.edit_message_text(text, reply_markup=InlineKeyboardMarkup(keyboard))

# --- HELP ---
async def help_page(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    text = (
        "❓ NEED HELP?\n\n"
        "Contact Digi-Bridge support:\n👉 @digibridge1\n\n"
        "Include your name and explain your issue clearly."
    )
    keyboard = [[InlineKeyboardButton("⬅️ Back to Main Menu", callback_data="main")]]
    await query.edit_message_text(text, reply_markup=InlineKeyboardMarkup(keyboard))

# --- COPY BUTTON HANDLERS ---
async def copy_cbe(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer("CBE account copied ✅")
    await query.message.reply_text("1000510260752")

async def copy_telebirr(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer("Telebirr phone copied ✅")
    await query.message.reply_text("0965080186")

async def copy_boa(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer("BOA account copied ✅")
    await query.message.reply_text("1030700179656")

# --- MAIN MENU RETURN ---
# --- MAIN MENU RETURN ---
async def main_menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    await start(update, context)

def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(about, pattern="about"))
    app.add_handler(CallbackQueryHandler(available, pattern="available"))
    app.add_handler(CallbackQueryHandler(join, pattern="join"))
    app.add_handler(CallbackQueryHandler(help_page, pattern="help"))
    app.add_handler(CallbackQueryHandler(copy_cbe, pattern="copy_cbe"))
    app.add_handler(CallbackQueryHandler(copy_telebirr, pattern="copy_telebirr"))
    app.add_handler(CallbackQueryHandler(copy_boa, pattern="copy_boa"))
    app.add_handler(CallbackQueryHandler(main_menu, pattern="main"))

    app.run_polling()

if __name__ == "__main__":
    main()
