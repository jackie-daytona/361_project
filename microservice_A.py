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
    obj = json.loads(data)
    if len(obj) >= 2:           # send sku alert to main program
        sku, quantity = obj
        alert = f"Item {sku} low in stock! Only {quantity} remaining."
        socket.send_string(alert)
        time.sleep(3)
    else:                       # else send confirmation message and end microservice
        if obj == "Q":
            socket.send_string("evaluation complete")
            print("message received")
            break

context.destroy()
