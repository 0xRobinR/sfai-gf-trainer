import json
import os
from xmlrpc.server import SimpleXMLRPCServer

import professor

connected_workers = 0
total_expected_workers = 1


def register_worker():
    global connected_workers
    connected_workers += 1
    print(f"Worker connected. Total connected workers: {connected_workers}")
    if connected_workers >= total_expected_workers:
        print("All workers are connected.")
        return True
    return False


server = SimpleXMLRPCServer(("localhost", 8000))
print("Listening on port 8000...")
server.register_function(register_worker, "register_worker")

# Wait for workers to connect and register
server.serve_forever()

tf_config = {
    'cluster': {
        'worker': ["localhost:8088"],
        'ps': ["localhost:8089"]
    },
    'task': {'type': 'ps', 'index': 0}
}

os.environ['TF_CONFIG'] = json.dumps(tf_config)

prof_node = professor.Professor("0x....000")  # professor address

# listen for events
prof_node.listen_for_events()

# call to professor node to train the model
prof_node.train_fetch_data("./data/")  # data path
# call to professor node to train the model
prof_node = professor.Professor("0x1234567890")
prof_node.train_fetch_data("./data/")
