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

while True:
    sample = [i]
    outlet.push_chunk(sample)
    print(f"Sent to Pong: {sample}")

    time.sleep(5)

    sample, timestamp = inlet.pull_chunk(timeout=0.0)

    while sample is None:     
        sample, timestamp = inlet.pull_chunk(timeout=0.0)    


    print(f"Received from Pong: {sample}, at {timestamp}")
    
    time.sleep(1)

    i += 1