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
    sample, timestamp = inlet.pull_chunk(timeout=0.0)

    if sample is not None and len(sample) != 0:
        print(f"Received from Ping: {sample} at {timestamp}")

        outlet.push_chunk(sample)
        print(f"Sent to Ping: {sample}")

    # Sleep to simulate time between responses
    time.sleep(1)
