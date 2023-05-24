import curses

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
print('try')
print('trying')
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
print('AAAAA')

textfieldObj = curses.newwin(textfield[3], textfield[2], textfield[1], textfield[0])
textfieldObj.keypad(True)
textfieldObj.box()
#textfieldObj = curses.pad(textfield[1], textfield[0])
#textfieldObj.box()

inputBoxObj = curses.newwin(window3[3], window3[2], window3[1], window3[0])
inputBoxObj.box()
inputTextpad = curses.textpad.Textbox(inputBoxObj)
#inputTextpad.edit()


textPadObj = curses.newpad(textfieldHeight - 1 ,textfieldWidth - 1)
textPadObj.scrollok(True)
#textPadObj.box()
sidePadObj = curses.newpad(sidebar1Height - 1,sidebar1Width - 1)
sidePadObj.scrollok(True)
#inputPadObj = curses.newpad( window3Height - 1,window3Width - 1 )


#except Exception as err:
#    caughtExceptions = str(err)
#
#    curses.nocbreak()
#    curses.echo()
#    curses.curs_set(True)

#    curses.endwin()




def getSidebar():
  return sidebarObj
def getTextField():
  return textfieldObj
def getInputBox():
  return inputBoxObj
def getTextPad():
  return textPadObj
def getSidePad():
  return sidePadObj
#def getInputPad():
#  return inputPadObj
