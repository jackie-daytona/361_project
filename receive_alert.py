import json
import zmq

food = {"654232": 8, "4334": 2}


def receive_alert():
    """
    communicates with sku_alert (microservice A) using zeromq
    code adapted from "Introduction to ZeroMQ" by Luis Flores
    """
    context = zmq.Context()
    # print("checking sku status...")

    socket = context.socket(zmq.REQ)
    socket.connect("tcp://localhost:5555")
    # print(f"sending request...")

    # change value within dumps() to match main program
    json_obj = json.dumps(food)
    socket.send_json(json_obj)

    # receive sku alert from microservice, print message to user
    message = socket.recv()
    print(f"{message.decode()}")

    socket.send_string("Q")


receive_alert()
