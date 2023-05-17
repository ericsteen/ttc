import twitchio
import asyncio
import ueberzug.lib.v0 as ueberzug
#import ueberzug
import curses
import curses.textpad
import math
import random
import sys


# Enter your Twitch credentials here
BOT_NICK = 
OAUTH_TOKEN = 
CHANNEL = 


print('curses init')
stdscr = curses.initscr()
curses.noecho()
curses.cbreak()
curses.curs_set(False)
if curses.has_colors():
  curses.start_color()
curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_MAGENTA)
curses.init_pair(2, curses.COLOR_BLACK, curses.COLOR_WHITE)
curses.init_pair(3, curses.COLOR_BLACK, curses.COLOR_GREEN)
print("HELLO")
caughtExceptions = ""
try:
    sidebar1Width = 25
    sidebar1Height = curses.LINES - 5
    textfieldWidth = curses.COLS - sidebar1Width
    textfieldHeight = curses.LINES - 5
    window3Width = curses.COLS
    window3Height = 5
    sidebar1 = [0,0, sidebar1Width, sidebar1Height]
    textfield = [sidebar1Width,0,textfieldWidth,textfieldHeight]
    window3 = [0, curses.LINES-5, window3Width, window3Height]

    sidebarObj = curses.newwin(sidebar1[3], sidebar1[2], sidebar1[1], sidebar1[0])
    sidebarObj.box()

    textfieldObj = curses.newwin(textfield[3], textfield[2], textfield[1], textfield[0])
    textfieldObj.keypad(True)
    textfieldObj.box()

    inputBoxObj = curses.newwin(window3[3], window3[2], window3[1], window3[0])
    inputBoxObj.box()

except Exception as err:
    caughtExceptions = str(err)

    curses.nocbreak()
    curses.echo()
    curses.curs_set(True)

    curses.endwin()


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




def getSidebar():
  return sidebarObj
def getTextField():
  return textfieldObj
def getInputBox():
  return inputBoxObj
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
    sidebarObj.addstr(username + '\n')
    textfieldObj.addstr('\t' + message + '\n')
    #inputBoxObj.addstr(username + ' : ' + message)

c = ueberzug.Canvas()

async def main():

    #messagecount = 0
    #initCurses()
    textfield = getTextField()
    sidebar = getSidebar()
    client = MyClient()
    #sidebar.addstr('this is the sidebar')
    inputbox = getInputBox()

    await client.connect()
    while True:
        try:
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

