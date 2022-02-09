import pulsar

client = pulsar.Client('pulsar://pulsar1:6650')

producer = client.create_producer('persistent://public/default/pi-logs')

for i in range(10):
    producer.send(('Hello this is great news-%d' % i).encode('utf-8'))

client.close()
