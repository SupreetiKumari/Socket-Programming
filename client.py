import socket, pickle

SERVER = "127.0.0.1"
PORT = 8080
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((SERVER, PORT))
out_dat = []

while True:
    n = int(input("The number of elements: "))
    for i in range(n):
        out_dat.append(int(input("  Enter the number: ")))
    out_data = pickle.dumps(out_dat)
    client.sendall(out_data)
    if n == 0:
        break
    in_data =  client.recv(2048)
    ind = pickle.loads(in_data)
    print("The Answer is :" ,ind[0])
    out_dat.clear()
client.close()
