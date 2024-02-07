import socket
from threading import Thread

PORT = 50000
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
SERVER = "localhost"
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)
name = ""


def read():
    while True:
        rec = client.recv(1024).decode(FORMAT)
        if rec.split(":")[0] == name:
            continue
        print(rec)


def send(msg):
    if msg == "!d":
        msg = DISCONNECT_MESSAGE
    message = bytes(msg, FORMAT)
    client.send(message)


def start():
    global name
    thread = Thread(target=read, args=())
    thread.daemon = True
    thread.start()
    name = input("Name: ")
    send(name)
    while True:
        send(input())


start()
