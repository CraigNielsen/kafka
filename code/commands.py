#!/usr/bin/env python
import os
import sys

run = os.system
print(sys.argv)

if sys.argv[1] == 'create':
    run('docker run --rm -it --net=host landoop/fast-data-dev bash -c "kafka-topics --zookeeper 127.0.0.1:2181 --create --topic {}  --partitions 3 --replication-factor 1"'.format(sys.argv[2]))

if sys.argv[1] == 'list':
    run('docker run --rm -it --net=host landoop/fast-data-dev bash -c "kafka-topics --zookeeper 127.0.0.1:2181  --list')

if sys.argv[1] == 'describe':
    run('docker run --rm -it --net=host landoop/fast-data-dev bash -c "kafka-topics --zookeeper 127.0.0.1:2181  --describe --topic {}'.format(sys.argv[2]))
