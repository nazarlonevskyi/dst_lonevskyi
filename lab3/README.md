# dst_lonevskyi
***
## Distributed Systems Seminars: 2. TCP Sockets

1. To run server and client you need use `Java` version `1.8` or higher and `Maven` tool.

2. First of all you have to start the server. To do this, run the following command in folder with TCPsocket, for which you can specify your IP-address and port (for example):
    ```
    mvn clean compile exec:java -D exec.args="127.0.0.1 4000"
    ```
3. Then you can start the client. To do this, run the same command with the same argument as for the server in folder with client.

4. You can send the command to the server after running the client. List and description of the available commands can be seen by running the `help` command. Following commands are available for the client:
    
    - `exit` - shutdown client (no parameters);
    - `ping` - testing connection (no parameters);
    - `echo` - testing sending message. After entering the command, the program will ask you to enter text of echo message:
        ```
        Enter the command (help - list of available commands):
        echo
        You choose the command echo.
        Enter the echo text: Hello world
        ```
    
5. Application prints when some new user logs in to the server and logs out of the server:
    - To check it you need to log in to several accounts from different terminals:
    ``` 
    ~~~Terminal_1~~~
    Enter the command (help - list of available commands):
    login
    You choose the command login.
    Enter the login: user1
    Enter the password: pass
    Server answer:
    Successful login.
    ```
    ```
    ~~~Terminal_2~~~
    Enter the command (help - list of available commands):
    login
    You choose the command login.
    Enter the login: user2
    Enter the password: pass
    Server answer:
    Successful login.
    ```
    ```
    ~~~Terminal_1~~~
    Enter the command (help - list of available commands):
    The user user2 connected to the server.
    exit
    ```
    ```
    ~~~Terminal_2~~~
    Enter the command (help - list of available commands):
    The user user1 disconnected from server
    ```
