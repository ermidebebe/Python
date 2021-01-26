import socket             
import matplotlib.pyplot as plt
import numpy as np
# Create a socket object  
s = socket.socket()       
  
# Define the port on which you want to connect  
port = 12345                
  
# connect to the server on local computer  
s.connect(('192.168.43.123', port))  
while True:
    # receive data from the server
    plt.imshow(s.recv(10240))
    plt.show()
# close the connection  
s.close() 
