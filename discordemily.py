from chatterbot import ChatBot
import datetime
import discord
from time import sleep

name = "Gus"
username = "Boris"
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

bot = ChatBot(
    'Emily',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    logic_adapters=[
        'chatterbot.logic.BestMatch'
    ],
    database_uri='sqlite:///coldai.db'
)

def incomingreplace(string):
    string = string.lower()
    string = string.replace(name, "[0x02]") 
    string = string.replace(username, "[0x01]")
    string = string.replace("afternoon", "[0x03]")
    string = string.replace("morning", "[0x03]")
    string = string.replace("evening", "[0x03]")
    for index, item in enumerate(days):
        if index == datetime.datetime.today().weekday():
            string = string.replace(item, "[0x06]")
    return string

def outgoingreplace(string):
    string = str(string).lower()
    string = string.replace("[0x01]", name)
    string = string.replace("[0x02]", username)
    
    timehour = datetime.datetime.now().hour
    if timehour < 12:
        aftmorneven = "morning"
    elif timehour > 12 and timehour < 18:
        aftmorneven = "afternoon"
    else:
        aftmorneven = "night"
    string = string.replace("[0x03]", aftmorneven)
    dayint = datetime.datetime.today().weekday()
    string = string.replace("[0x06]", days[dayint])
    return string

def getresponsereal(stri):
    user_input = ""
    user_input = stri
    if user_input != "[0x07]":
        user_input = incomingreplace(user_input)
        bot_response = bot.get_response(user_input)
        bot_response = outgoingreplace(bot_response)
        print("[Debug] Emily: " + str(bot_response))
        return str(bot_response)


print("Emily v0.1")
print("Slapped together by 1Somebody5")
print("")
print("Thanks to the following librarys:")
print("Chatterbot by Gunther Cox")
print("Pyttsx3 by Natesh M Bhat")
print("Speech_recognition by Anthony Zhang")
print("")
print("Initilizing...")



class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):
        if message.author == self.user:
            return

        if message.channel == client.get_channel(592092358443794472):
            channel = message.channel
            #async with channel.typing():
            async with channel.typing():
                await channel.send(getresponsereal(message.content))
                # user_input = ""
                # user_input = message.content
                # if user_input != "[0x07]":
                #     user_input = incomingreplace(user_input)
                #     bot_response = bot.get_response(user_input)
                #     bot_response = outgoingreplace(bot_response)
                #     print("[Debug] Emily: " + str(bot_response))
                #     #message.respond(bot_response)

client = MyClient()
client.run('uwu token go here')
