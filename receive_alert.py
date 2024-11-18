import json
import zmq

food = {"767": 8, "654": 10, "4334": 2, "76998": 10, "273": 1}


def receive_alert(low_item):
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
    json_obj = json.dumps(low_item)
    socket.send_json(json_obj)

    # receive sku alert from microservice, print message to user
    message = socket.recv()
    print(f"{message.decode()}")

    # socket.send_string("Q")


for sku, quantity in food.items():
    if quantity < 5:
        receive_alert((sku, quantity))
receive_alert("Q")
