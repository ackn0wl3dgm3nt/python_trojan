import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("127.0.0.1", 8888))
s.listen(5)

client, addr = s.accept()

while True:
    command = str(input("Enter command >> "))
    if command.lower() == "exit":
        break
    client.send(command.encode())

client.close()
s.close()
