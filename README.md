# server
			

Introduction
I designed a multiplayer quiz game. The rules are stated in the code at the start of the game. For this, I used Python threading.

Idea
The idea was to have the players as clients, who connect to a server which sets up a private multiplayer room and each are asked questions. When the client answers correctly, he/she gets a point and the game advances to the next question.
			
Implementation
To implement this, I used the concept of setting a chat room using python threads. This helps to treat each client as the only one present, and deal with all of them by calling the functions in a for loop. This loop forwards the questions to other clients. 
 
Working
To start the server, we call 
                                           python server.py  <ip-address> <port number> 
 and to play the game we call
                                           python client.py

The rules will be displayed at the start of the game. When the maximum number of players have joined (which can be set in the server.py function), the game will start. A questionaire will ask all the questions with a time gap between each question. There will be 5 questions shown to you. Whoever scores 3 points first will win.

 Procedure
    • A client must wait 3 seconds for the next question to pop up.
    • Questions from general knowledge.
    • In case of a tie, all players with the highest score win.
    • Server receives a log of everything that happens in the client side.
    • Your answer will be appropriately marked.
    • You are not told whether you are right or wrong when you answer and only find out your final score.


References
    • https://www.geeksforgeeks.org/simple-chat-room-using-python/


