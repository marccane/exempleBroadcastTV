#!/bin/env python3
import socket
import threading

def receive_broadcast_message(port):
  # Create a UDP socket
  sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
  # Enable broadcasting mode
  sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
  # Bind to all interfaces and the specified port
  sock.bind(('', port))
  print("Server listening for broadcast messages...")

  while True:
    # Receive a message
    data, addr = sock.recvfrom(1) #Número de bytes que volem rebre del broadcast

    print(f"Received broadcast message from {addr}: {data.decode()}")

if __name__ == "__main__":
  # Port for broadcasting and receiving messages
  port = 12345
  # Start a thread to receive broadcast messages
  receive_thread = threading.Thread(target=receive_broadcast_message, args=(port,))
  receive_thread.start()
