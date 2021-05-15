import pulsar

client = pulsar.Client('pulsar://localhost:6650')

producer = client.create_producer('my-topic')

for i in range(100):
    producer.send(('Hello-%d' % i).encode('utf-8'))

client.close()
