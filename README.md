### Task 3. Socket programming (Python)
Your CIO assigns you another project which involves setting up of connections between many clients and one server. 
- First of all, write a program that facilitates one client communicating with the server, in separate windows. 

- Secondly, while the first client is running, start 10 other clients that connect to the same server; these clients should most likely be started in the background with their input redirected from a file. Report what happens to these 10 clients? Do their connect()s fail, or time out, or succeed? Do any other calls block? Now let the client exit. Explain what happens.

- Thirdly, modify the socket program so that each time the client sends a line to the server, the server sends the line back to the client. The client (and server) will now have to make alternating calls recv () and send ().

- Finally, modify the socket program so that it uses UDP as the transport protocol, rather than TCP. You will have to change SOCK_STREAM to SOCK_DGRAM in both the client and the server. Discuss what happens when two UDP clients simultaneously connect to the same UDP server and compare this to the TCP behaviour.