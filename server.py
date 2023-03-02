import time, socket, sys

print("Welcome to chat room server side")
print("Initialising.....\n")

time.sleep(1)

s = socket.socket() # creates socket using address family, socket type and protocol
host = socket.gethostname()
ip = socket.gethostbyname(host) #gets machine IP address
port = 1234
s.bind((host, port)) #binds port to a given address 
print(host, "(", ip, ")\n")

s_name = input("Enter your name > ")
s.listen(1) # means only one connection is kept waiting and if server is busy the connection is refused
print("\nWaiting for incoming connections......\n")
conn, addr = s.accept()
print("Recieved connection from ", addr[0], " port: ", addr[1])

c_name = conn.recv(1024)
c_name = c_name.decode()
print(c_name," has entered the chat room")
print("Enter [e] to exit the chat room")
conn.send(s_name.encode())


while True:
    message = input("Me ({}) > ".format(s_name))
    if message == "[e]":
        message = s_name + " left chat room"
        conn.send(message.encode())
        print()
        break
    conn.send(message.encode())
    message = conn.recv(1024)
    message = message.decode()
    print(c_name, " > ", message)

