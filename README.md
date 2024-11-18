Communication Contract:

A. To request data from Microservice A, create a json object from your data and send it to the microservice. An example call would be:
        json_obj = json.dumps(food)
        socket.send_json(json_obj)
    Once you've established the proper connection with ZeroMQ (the "Introduction to ZeroMQ" pdf in Assignment 4 has a template), convert your data to a json object then use socket.send_json() to request data from the microservice.
    
B. Receiving data is the about the same as requesting: use ZeroMQ and call message = socket.recv() and print(f"{message.decode()}") to get the alert back from the microservice.

C. ![image](https://github.com/user-attachments/assets/053290a2-19b4-4a2d-a528-cc45f1f5d3ac)

