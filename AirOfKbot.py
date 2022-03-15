import telebot;

bot = telebot.TeleBot('5133581618:AAEOO5r7JO7-gK5xmTWhFkwnnz9qQbMgH9E');


def cmdHelp( msg ):
    bot.send_message( msg.from_user.id,  'This is AirOfK bot' )
    
def cmdRegister( msg ):
    bot.send_message( msg.from_user.id,  'Stub: register a station' )
    
def cmdStatus( msg ):
    bot.send_message( msg.from_user.id, 'Stub: current status is UNKNOWN' )
    
def cmdDefault( msg ):
    bot.send_message( msg.from_user.id, 'Sorry, I don\'t know this command' )


commandDict = {
    "help": cmdHelp,
    "register": cmdRegister,
    "status": cmdStatus 
}

@bot.message_handler( content_types=['text'] )
def get_text_messages( message ):
    commandDict.get( message.text, cmdDefault )( message )
    
    
bot.polling( none_stop = True, interval = 0 )
