import socket
import threading

def send_broadcast_message(message, port):
  # Create a UDP socket
  sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
  # Enable broadcasting mode
  sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
  # Send the message to the broadcast address
  sock.sendto(message.encode(), ('<broadcast>', port))
  # Close the socket
  sock.close()

if __name__ == "__main__":
  # Port for broadcasting and receiving messages
  port = 12345

  # Send a broadcast message
  message = "Hello from the server!"
  send_broadcast_message(message, port)
