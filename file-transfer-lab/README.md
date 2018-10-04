# file-transfer-lab

*   `stammerProxy.py` forwards tcp streams. It may delay the transmission of data but ensures all data will be forwarded, eventually.
   By default,
   it listens on port 50000 and forwards to localhost:50001.  

*  `fileClient.py` when ran, it connects to port 50001 by default unless specified otherwise. When connected it prompts the user for a file he wants stored in the Server. Multiple clients can be ran at the same time.

*  `fileServer.py` binds an address and listens defaultly on port 50001. It waits for one or several clients to connect on the port. It waits for the client to send a file and prints it out in the shell. It also stores the file in the Server folder as `myfile.txt`.

*  `framedSock.py` holds the common code used in the client and server including framed send and receive.

To run the file transfer program, open at least two shells (one for server and one for client). First run `./fileServer.py` on the first shell. The server will be listening for a client. On the second shell, run `./fileClient.py`. The client will prompt you to send a file. If the file is non existent the client will let you know. To run multiple clients, open more shells and run the client command. To specify port number, open another shell and run `./stammerProxy.py` after the Server and before the Client.
To specify port in the Server, type `./fileServer.py -l localhost:(port_#)` in the client `./fileClient.py -s localhost:(port_#)`.

