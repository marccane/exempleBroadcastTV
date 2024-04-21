import socket
import threading

# import RPi.GPIO as GPIO
# import time

# Set GPIO mode (BCM or BOARD)
# GPIO.setmode(GPIO.BOARD)

# Set the GPIO pin number
led_pin = 8

def send_broadcast_messagesend_broadcast_message(message, port):
  # Create a UDP socket
  sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
  # Enable broadcasting mode
  sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
  # Send the message to the broadcast address
  sock.sendto(message.encode(), ('<broadcast>', port))
  # Close the socket
  sock.close()

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
    data, addr = sock.recvfrom(1024)
    print(f"Received broadcast message from {addr}: {data.decode()}")
    # GPIO.output(led_pin, GPIO.HIGH)

if __name__ == "__main__":
  # Port for broadcasting and receiving messages
  port = 12345
  # Start a thread to receive broadcast messages
  receive_thread = threading.Thread(target=receive_broadcast_message, args=(port,))
  receive_thread.start()
  # Send a broadcast message
  message = "Hello from the server!"
  send_broadcast_message(message, port)
