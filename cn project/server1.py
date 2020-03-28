import socket
import select
import thread
import sys
import time
import random

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

if len(sys.argv) != 3:
    print("Correct usage: script, IP address, port number")
    exit()

IP_address = str(sys.argv[1])
Port = int(sys.argv[2])
server.bind((IP_address, Port)) 
server.listen(100)

list_of_clients=[]

Q = ['Q1','Q2','Q3','Q4','Q5','Q6','Q7','Q8','Q9','Q10','Q11','Q12','Q13','Q14','Q15','Q16','Q17','Q18','Q19','Q20']
A = ['a','b','c','d','a','a','b','c','d','a','a','b','c','d','a','a','b','c','d','a']
Count=[]
client = ["address",-1]
buz =[0, 0, 0]

while True:
    conn, addr = server.accept()
    """
    Accepts a connection request and stores two parameters, conn which is a socket object for that user, and addr which contains
    the IP address of the client that just connected
    """
    list_of_clients.append(conn)
    Count.append(0)
    print(addr[0] + " connected")
    #maintains a list of clients for ease of broadcasting a message to all available people in the chatroom
    #Prints the address of the person who just connected
    thread.start_new_thread(clientthread,(conn,addr))
    if(len(list_of_clients)==3):
        quiz()

def clientthread(conn, addr):
    conn.send("Welcome to this Quiz!\n")
    #sends a message to the client whose user object is conn
    while True:
                
            message = conn.recv(2048)  
                
            if message:
                if buz[0]==0:
                    client[0] = conn
                    buz[0] = 1
                    i = 0
                    while i < len(list_of_clients):
                            if list_of_clients[i] == client[0]:
                                break
                            i +=1
                    client[1] = i

                elif buz[0] ==1 and conn==client[0]:
                    
                        bol = message[0] == A[buz[2]][0]
                        print(A[buz[2]][0]) 
                        if bol:
                            broadcast("player" + str(client[1]+1) + " +1" + "\n")
                            Count[i] += 1
                            if Count[i]==2:
                                gameover()
                                
                        else:
                            broadcast("player" + str(client[1]+1) + " -1" + "\n")
                            Count[i] -= 1
                        buz[0]=0
                        
                        if len(Q) != 0:
                            Q.pop(buz[2])
                            A.pop(buz[2])
                        if len(Q)==0:
                            gameover()
                        quiz()

                else:
                        conn.send("player " + str(client[1]+1) + ",buzzer has been pressed.\n")
            else:
                    remove(conn)

def gameover():
        broadcast("GAME OVER!\n")
        buz[1]=1
        j = Count.index(max(Count))
        broadcast("player " + str(j+1)+ " wins by scoring "+str(Count[j])+" points.")
        for i in range(len(list_of_clients)):
            list_of_clients[i].send("You scored " + str(Count[i]) + " points.")
            list_of_clients[i].exit()
        server.close()

def broadcast(message):
    for clients in list_of_clients:
        try:
            clients.send(message)
        except:
            clients.close()
            remove(clients)

def remove(connection):
    if connection in list_of_clients:
        list_of_clients.remove(connection)

def quiz():
    buz[2] = random.randint(0,10000)%len(Q)
    if len(Q) != 0:
        for connection in list_of_clients:
            connection.send(Q[buz[2]])
        

conn.close()
server.close()
