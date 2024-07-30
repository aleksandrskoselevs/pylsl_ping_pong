# Setup

import time
from pylsl import StreamInlet, StreamOutlet, StreamInfo, resolve_byprop

info = StreamInfo('PongStream', 'Markers', 1, 0, 'int32', 'pong_stream')
outlet = StreamOutlet(info)
print("Pong stream created.")

print("Looking for a Ping stream...")
streams = None
while streams is None:
    streams = resolve_byprop('name', 'PingStream')
    if not streams:
        print("No Ping stream found, retrying...")
        time.sleep(1)

inlet = StreamInlet(streams[0])
print("Ping stream found.")



# Interaction loop

while True:
    # Receive a sample from the Ping stream
    incoming_sample, timestamp = inlet.pull_chunk(timeout=0.0)

    if incoming_sample is not None and len(incoming_sample) != 0:
        print(f"Received from Ping: {incoming_sample} at {timestamp}")

        outgoing_sample = incoming_sample
        
        outlet.push_chunk(outgoing_sample)
        print(f"Sent to Ping: {outgoing_sample}")

    # Sleep to simulate time between responses
    time.sleep(1)
