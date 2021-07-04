import socket, pickle

def sumarr(array):
    sum = 0
    for l in array:
        sum += l
    return sum

SERVER = "127.0.0.1"
PORT = 8080
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((SERVER, PORT))


while True:
    l = []
    in_data =  client.recv(2048)
    real_msg = pickle.loads(in_data)
    print("From Server :" ,real_msg)
    out_data = sumarr(real_msg)
    l.append(out_data)
    print ("The Sum is: ",l)
    out = pickle.dumps(l)
    client.sendall(out)
client.close()
