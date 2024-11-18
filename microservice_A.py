# Danny Caspary
# CS361: Microservice A -- SKU alert
# Fall 2024
# Using ZeroMQ API, code adapted from example in "Introduction to ZeroMQ"
#     by Luis Flores

import zmq
import time
import json

context = zmq.Context()

socket = context.socket(zmq.REP)

socket.bind("tcp://*:5555")

while True:
    data = socket.recv_json()

    if len(data) > 0:
        obj = json.loads(data)
        for sku, quantity in obj.items():
            if quantity < 5:
                alert = f"Item {sku} low in stock! Only {quantity} remaining."
                socket.send_string(alert)
        time.sleep(3)

    message = socket.recv()
    print(f"received request from the client: {message.decode()}")
    if len(message) > 0:
        if message.decode() == "Q":
            break

context.destroy()
