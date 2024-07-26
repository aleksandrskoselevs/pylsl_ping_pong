import time
import logging
from pylsl import StreamInlet, StreamOutlet, StreamInfo, resolve_byprop

from pylsl import resolve_stream

# Setup logging
# logging.basicConfig(level=print)

# Define the ping stream
info = StreamInfo('PingStream', 'Markers', 1, 0, 'int32', 'ping_stream')
outlet = StreamOutlet(info)
print("Ping stream created.")

# Delay to ensure Pong stream is ready
time.sleep(5)

# Resolve the Pong stream
print("Looking for a Pong stream...")
streams = None
while streams is None:
    streams = resolve_byprop('name', 'PongStream')
    if not streams:
        print("No Pong stream found, retrying...")
        time.sleep(1)

inlet = StreamInlet(streams[0])
print("Pong stream found.")

# 0 when sent from Pong to Ping, Ping prints it out as an empty array
i = 1

while True:
    sample = [i]
    outlet.push_sample(sample)
    # outlet.push_chunk(sample)
    print(f"Sent to Pong: {sample}")

    time.sleep(5)

    # Receive a sample from the Pong stream
    
    # This continues sending, even if the Pong died
    # sample, timestamp = inlet.pull_sample(timeout=2)

    # This stops everything
    # sample, timestamp = inlet.pull_sample()
    # sample, timestamp = inlet.pull_chunk()

    # # This works, but sends signals ignoring the response
    # sample, timestamp = inlet.pull_sample(timeout=0.0)

    # while sample is None:
    #     sample, timestamp = inlet.pull_sample(timeout=0.0)

    sample, timestamp = inlet.pull_chunk(timeout=0.0)

    # This works, but first sample is empty array
    while sample is None:
      
    # This stops
    # while sample is None or len(sample) == 0:
        sample, timestamp = inlet.pull_chunk(timeout=0.0)    
    
    # if sample is not None:
    #     print(f"Received from Pong: {sample}")

    print(f"Received from Pong: {sample}, at {timestamp}")


    # Sleep to simulate time between responses
    time.sleep(1)

    i += 1
