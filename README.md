# PyLSL Ping-Pong

Minimal working demo of a back and forth with pylsl.

1. Launch pong.py
2. Launch ping.py (in a separate terminal)
   
**Flow**
- Ping sends a number to Pong.
- Pong sends the same number back to Ping.
- Ping then increases that number by 1. And it begins again.

This is managed through 2 streams.

**Expected output**

`ping.py`

```python
...
Ping stream created.
Looking for a Pong stream...
Pong stream found.
Sent to Pong: [1]
Received from Pong: [[1]] at [319129.0189355]
Sent to Pong: [2]
Received from Pong: [[2]] at [319130.024301041]
Sent to Pong: [3]
Received from Pong: [[3]] at [319131.029552083]
...
```

`pong.py`
```python
...
Pong stream created.
Looking for a Ping stream...
Ping stream found.
Received from Ping: [[1]] at [319128.240374166]
Sent to Ping: [[1]]
Received from Ping: [[2]] at [319129.246480333]
Sent to Ping: [[2]]
Received from Ping: [[3]] at [319130.250781541]
Sent to Ping: [[3]]
....
```
