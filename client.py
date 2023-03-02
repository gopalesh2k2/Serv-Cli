import time, socket

print("Welcome to client side chat room")
print("Initializing.....")
time.sleep(1)
sok = socket.socket()
host = socket.gethostname()
ip = socket.gethostbyname(host)
print(host, " (", ip, ")")
# server ip is 10.103.51.28
s_host = input("Enter server IP address > ")
clientName = input("Enter your name > ")
port = 1234
print("Trying to connect to ", s_host, " ( ", port, " )")
time.sleep(1)
sok.connect((s_host, port))
print("Connected")
sok.send(clientName.encode())
s_name = sok.recv(1024)
s_name = s_name.decode()
print(s_name, "has joined the chat room\nEnter [e] to exit chat room\n")


while True:
    message = sok.recv(1024)
    message = message.decode()
    print(s_name, " > ", message)
    message = input("{} > ".format(clientName))
    if message == "[e]":
        message = "Left chat room!"
        sok.send(message.encode())
        print("\n")
        break
    sok.send(message.encode())
