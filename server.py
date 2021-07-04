import socket, threading, os, pickle
N = 4
all_msgs = []
minion_sums = []

def sumarr(array):
    sum = 0
    for l in array:
        sum += l
    return sum

def dividearr(array,n):
    result_arr = []
    for i in range(n):
        result_arr.append([])
    m = len(array)
    q = int(m/n)
    for j in range(0,q*n):
        result_arr[int(j/q)].append(array[j])
    for i in range(q*n,m):
        result_arr[i-(q*n)].append(array[i])
    return result_arr

class ClientThread(threading.Thread):
    def __init__(self,clientAddress,clientsocket):
        threading.Thread.__init__(self)
        self.csocket = clientsocket
        # self.running = True
        print ("Client connection added: ", clientAddress)
    def run(self):
        msg = ''
        while True:
            data = self.csocket.recv(2048)
            msg = pickle.loads(data)
            all_msgs.append(msg)
            if len(msg) == 0:
                break
            print ("Input Array: ", msg)

            if len(all_msgs)>0:
                dividearr(msg,N)
                division_arr = dividearr(msg,N)

                for i in range(0,N):
                    os.system("gnome-terminal -e 'python minion.py'")
                    clientsock, clientAddress = server.accept()
                    minithread = MinionThread(clientAddress, clientsock)
                    minithread.start()
                    threads.append(minithread)
                    minionthreads.append(minithread)
                    di = pickle.dumps(division_arr[i])
                    minithread.csocket.sendall(di)
                all_msgs.remove(all_msgs[0])
                msg.clear()

        print ("Client disconnected...")
        print("To start again run the server again ")
 

class MinionThread(threading.Thread):
    def __init__(self,clientAddress,clientsocket):
        threading.Thread.__init__(self)
        self.csocket = clientsocket
        print ("Minion Called ", clientAddress)
    def run(self):
        msg = ''
        while True:
            data = self.csocket.recv(2048)
            msg = pickle.loads(data)
            minion_sums.append(msg[0])
            print ("from ",clientAddress,": ",minion_sums[-1])
            if len(minion_sums)==N:
                l = []
                f_sum = sumarr(minion_sums)
                print("Sum: ",f_sum)
                l.append(f_sum)
                out = pickle.dumps(l)
                minthread.csocket.sendall(out)
                minion_sums.clear()
                msg.clear()
                minionthreads.clear()
        print ("Client at ", clientAddress , " disconnected...")

LOCALHOST = "127.0.0.1"
PORT = 8080

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((LOCALHOST, PORT))
threads = []
minionthreads = []
real_msg = []
server.listen(1+N)


print("Now, Open the client file....")
print("Server started")
print("Waiting for client request..")


clientsock, clientAddress = server.accept()
minthread = ClientThread(clientAddress, clientsock)
minthread.start()
threads.append(minthread)
