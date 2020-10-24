#!/bin/bash

docker run --gpus all -it -p 8888:8888 --net=host -v `pwd`:/tf tf
