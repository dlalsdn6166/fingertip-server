import socket
import myocr
import time
import threading
import signal
import myutil

address = '0.0.0.0'
port = 9879

def handleClient(client_socket:socket, client_address):
    print('!--- Request from {} ---!'.format(client_address))
    start = time.time()
    data = client_socket.recv(4)
    img_size = int.from_bytes(data, byteorder = 'big')    
    print('# image_size: {}'.format(img_size))
    data = client_socket.recv(img_size)
    result = myutil.encode(myocr.read(data))
    client_socket.sendall(len(result).to_bytes(4,byteorder = 'big'))
    client_socket.sendall(result)
    print('# result: {}\n# time_spent: {}'.format(result.decode(), time.time()-start))

def Terminate(signum, frame):
    print('Terminating program...')
    server_socket.close()

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_socket.bind((address, port))
signal.signal(signal.SIGINT, Terminate)
server_socket.listen(); # wait for client

print('waiting client on port {}'.format(port))
while True:
    client_socket, client_addr = server_socket.accept()
    th = threading.Thread(target=handleClient, args=(client_socket,client_addr))  
    th.start()
