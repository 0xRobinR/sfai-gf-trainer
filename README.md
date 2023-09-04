## School for AI

a project where AI can be trained decentralized, using the decentralized storage provider, BNB Greenfield.

### Setup

- Install the requirements

```shell
pip install - r requirements.txt
```

- Run the `parameter server` or professor nodes (`PN`), that will listen to the AI train requests from the BNB Chain

```shell
python main.py
```

- Once the PN is up and running, connect the worker nodes, this will be incharge
  of computing the model and maintaining a two-way communication with the professor nodes.

```shell
python .\workers\main.py
```

As the worker establishes the connection, the PN will coordinate with the given model and data, and using tensorflow's
`ParameterServerStrategy`, it will distribute the model to the workers, and will start the training process.

### Current State

- [ ] Currently, it’s all backend, will have to work on the user interface side as well

- [x] Professor nodes are listening to the events

- [x] Worker nodes are connected to the professor nodes

- [x] The model is distributed to the workers

- [ ] Downloading the files from Greenfield and then processing it locally, and then uploading the model with the user
  only
  access to the file (encrypted model)

- [ ] while downloading, the speed of accessing the resources is very slow.

Further, I need more help from the BNB Chain team, to get the things done and in the correct way.
