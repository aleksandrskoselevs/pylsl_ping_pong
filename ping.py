# Setup

import time
from pylsl import StreamInlet, StreamOutlet, StreamInfo, resolve_byprop

info = StreamInfo('PingStream', 'Markers', 1, 0, 'int32', 'ping_stream')
outlet = StreamOutlet(info)
print("Ping stream created.")

# Delay to ensure Pong stream is ready
time.sleep(5)

print("Looking for a Pong stream...")
streams = None
while streams is None:
    streams = resolve_byprop('name', 'PongStream')
    if not streams:
        print("No Pong stream found, retrying...")
        time.sleep(1)

inlet = StreamInlet(streams[0])
print("Pong stream found.")


# Interaction loop

i = 1

outgoing_sample = [i]
outlet.push_chunk(outgoing_sample)
print(f"Sent to Pong: {outgoing_sample}")

time.sleep(5)

while True:
    incoming_sample, timestamp = inlet.pull_chunk(timeout=0.0)

    # This halts, because the first sample is len 0
    # if sample is not None and len(sample) != 0:
    
    if incoming_sample is not None:
        print(f"Received from Pong: {incoming_sample} at {timestamp}")

        i += 1
        outgoing_sample = [i]
        
        outlet.push_chunk(outgoing_sample)
        print(f"Sent to Pong: {outgoing_sample}")

    # Sleep to simulate time between responses
    time.sleep(1)