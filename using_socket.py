import socket

# Create a socket to connect to the web server
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))

# Send an HTTP GET request to the server
cmd = 'GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n'
cmd = cmd.encode()
mysock.send(cmd)

# Receive and print the response, including headers and data
while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    print(data.decode(), end='')

# Close the socket
mysock.close()
