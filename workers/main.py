import os
import json

from worker import SFAIWorker

import xmlrpc.client

tf_config = {
    'cluster': {
        'worker': ["localhost:8088"],
        'ps': ["localhost:8089"]
    },
    'task': {'type': 'worker', 'index': 0}
}

os.environ['TF_CONFIG'] = json.dumps(tf_config)

with xmlrpc.client.ServerProxy("http://localhost:8000/") as proxy:
    print("Registering with parameter server...")
    if proxy.register_worker():
        print("All workers are connected. Starting training.")
        worker = SFAIWorker()
        worker.train("./data/")