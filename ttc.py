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
import random

global pad_y
pad_y = 0

# Enter your Twitch credentials here
OAUTH_TOKEN = ''
BOT_NICK = ''
CHANNEL = ''

#global emoteList
emoteList = []
#global emoteRequest
emoteRequest = False

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

def emoteUpdate():
    for emote in emoteList:
        emote.x += 1

def addEmote(object):
    if len(emoteList) > 10:
        emoteList.pop(0)
    emoteList.append(object)
    emoteRequest = True

def lexer(content): #just for testing purposes, will fix later
    words = content.split()
    count = 0
    for x in words:
      if x == 'Kappa':
        #addEmote(canvas.create_placement('', x=count, y=10, scaler=ueberzug.ScalerOption.COVER.value, path='../test/kappa.png'))
        global emoteRequest
        emoteRequest = True
        tc.getSidePad().addstr(str(emoteRequest) + '\n')
        tc.getTextPad().addstr(str(emoteRequest) + '\n')
      else:
          count += len(x)


def addMessage(username, Message):
    lexer(Message)
    tc.getSidePad().addstr(username + '\n')
    #tc.getSidePad().addstr('-----\n')
    tc.getTextPad().addstr(Message + '\n')
    #textfieldObj.addstr('\t' + message + '\n', curses.A_UNDERLINE)
    #inputBoxObj.addstr(username + ' : ' + message)
    emoteUpdate()

#@uberzug.Canvas()
async def main():
    with ueberzug.Canvas() as c:
#    demo = canvas.create_placement('textscreen', x=10, y=10)
        global emoteRequest
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
        demo = c.create_placement('demo',x=0,y=0,scaler=ueberzug.ScalerOption.COVER.value, path='../test/kappa.png')
        #pad_y += 1
        #inputpad = tc.getInputPad()
        #pad_y = 0

        await client.connect()
        while True:
            with c.lazy_drawing:
                try:
                    if emoteRequest:
                        addEmote(c.create_placement(random.randint(0,99999999), x=10, y=10, path='../test/kappa.png]'))
                        emoteRequest = False
                        tc.getSidePad().addstr(str(emoteRequest) + '\n')
                        tc.getTextPad().addstr(str(emoteRequest) + '\n')
                    textpad.refresh(0,0,1,27,23,185)
                    sidepad.refresh(0,0,1,1,23,22)
                    #inputpad.refresh(0,0,28,28,50,50)
                    textfield.refresh()
                    sidebar.refresh()
                    inputbox.refresh()
                    demo.x = demo.x + 1
                    demo.y = demo.y - 1
                    #cursesApp.getInputBox.getch()
                    await asyncio.sleep(1)
                except KeyboardInterrupt:
                    await client.close()
                    break

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())

