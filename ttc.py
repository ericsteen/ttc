import twitchio
import asyncio
import ueberzug.lib.v0 as ueberzug
#import ueberzug
import curses
import curses.textpad
import math
import random
import sys
import ttcCurses as tc

global pad_y
pad_y = 0

# Enter your Twitch credentials here
OAUTH_TOKEN = 'oauth:fg3bd5c7ecwd2f8kpiu2qpnllhlyoo'
BOT_NICK = 'skitz_gaming'
CHANNEL = 'monkeys_forever'


class MyClient(twitchio.Client):
    nick = BOT_NICK
    initial_channels=CHANNEL

    def __init__(self):
        super().__init__(token=OAUTH_TOKEN,  initial_channels=[CHANNEL])

    async def event_message(self, message):

        #print(f'{message.author.name} :\t {message.content}')
        #print("TESTTESTTEST")
        addMessage(message.author.name, message.content)

    async def event_ready(self):
        #print(f'Connected!')
        pass

    async def send_chat(self, text):
        await self.connected.channels[0].send(text)


#def parser2(message):
#    if len(message) >= 175:
#        return [string]
#    else:
#        return [string[:175]] + split_string_recursive(string[175:])
#def parser1(message):
#    list = parser2(message)
#    return ' '.join(str(x) for x in message)

def lexer(content): #just for testing purposes, will fix later
    words = content.split()
    count = 0
    for x in words:
      if x == 'Kappa':
        return count
      else:
        count = count + len(x)


def addMessage(username, message):
    #messagecount = messagecount + 1
    #if messagecount > 27:
    #  pass
    spot = lexer(message)
    if spot != None:
      Kappa = c.create_placement('Kappa', x=0, y=spot, scaler=ueberzug.ScalerOption.COVER.value)
      Kappa.path = './kappa.png'
    message = message[:175]
    tc.getSidePad().addstr(username + '\n')
    #tc.getSidePad().addstr('-----\n')
    tc.getTextPad().addstr(message + '\n')
    #tc.getTextPad().addstr('-----\n')
    #tc.getSidePad().scroll(-1)
    #tc.getTextPad().scroll(-1)
    #textfieldObj.addstr('\t' + message + '\n', curses.A_UNDERLINE)
    #inputBoxObj.addstr(username + ' : ' + message)

c = ueberzug.Canvas()

async def main():
    pad_y = 1
    #messagecount = 0
    #initCurses()
    textfield = tc.getTextField()
    sidebar = tc.getSidebar()
    client = MyClient()
    textpad = tc.getTextPad()
    sidepad = tc.getSidePad()
    #sidebar.addstr('this is the sidebar')
    inputbox = tc.getInputBox()
    pad_y += 1
    #inputpad = tc.getInputPad()
    #pad_y = 0

    await client.connect()
    while True:
        try:
            textpad.refresh(pad_y,0,1,27,25,75)
            sidepad.refresh(pad_y,0,1,1,50,45)
            #inputpad.refresh(0,0,28,28,50,50)
            textfield.refresh()
            sidebar.refresh()
            inputbox.refresh()
            #cursesApp.getInputBox.getch()
            await asyncio.sleep(1)
        except KeyboardInterrupt:
            await client.close()
            break

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())

