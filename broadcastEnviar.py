#!/bin/env python3
import socket
import threading

def send_broadcast_message(message, port):
  # Create a UDP socket
  sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
  # Enable broadcasting mode
  sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
  # Send the message to the broadcast address
  sock.sendto(message, ('<broadcast>', port))
  # Close the socket
  sock.close()

if __name__ == "__main__":
  # Port for broadcasting and receiving messages
  port = 12345

  while True:
    entradaUsuari = input("Tria una acció: 'on', 'off', 'canal': ")
    if entradaUsuari == "on":
      print("Enviant broadcast per engegar TV")
      send_broadcast_message((1).to_bytes(), port)
    elif entradaUsuari == "off":
      print("Enviant broadcast per apagar TV")
      send_broadcast_message((2).to_bytes(), port)
    elif entradaUsuari == "canal":
      print("Enviant broadcast per passar de canal")
      send_broadcast_message((3).to_bytes(), port)
    else:
      print("Acció no reconeguda")
