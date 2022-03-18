import telebot;

bot = telebot.TeleBot('');

helplist = {
    "help":     "Prints this message",
    "register": "Register your station",
    "status":   "Report status for the town",
    "ping":     "Check if the stations work",
    "get":      "Request data archive for a given day"
}


def cmdHelp(msg):
    bot.send_message(msg.from_user.id, 'This is AirOfK bot')


def cmdRegister(msg):
    bot.send_message(msg.from_user.id, 'Stub: cannot register a station now')


def cmdStatus(msg):
    bot.send_message(msg.from_user.id, 'Stub: current status is UNKNOWN')


def cmdPing( msg ):
    bot.send_message( msg.from_user.id, 'Stub: cannot see if all the stations are online')


def cmdGet( msg ):
    bot.send_message( msg.from_user.id, 'Stub: no data available for download' )


def cmdDefault(msg):
    bot.send_message(msg.from_user.id, 'Sorry, I don\'t know this command')


commandDict = {
    "help":     cmdHelp,
    "reg":      cmdRegister,
    "register": cmdRegister,
    "stat":     cmdStatus,
    "state":    cmdStatus,
    "status":   cmdStatus,
    "ping":     cmdPing,
    "get":      cmdGet
}

commandsOnly = list(commandDict.keys())


@bot.message_handler(commands=commandsOnly)
def get_text_messages(message):
    commandDict.get(message.text, cmdDefault)(message)


bot.polling(none_stop=True, interval=0)
