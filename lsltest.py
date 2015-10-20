import sys
from plugins.drivers.lsl.pylsl import StreamInlet, resolve_stream, resolve_bypred

# first resolve an EEG stream on the lab network
print("looking for an EEG stream...")

pred = "name='%s' and type='%s'" % ('NiDaq','emg')
streams = resolve_bypred(pred.encode('ascii'))


# create a new inlet to read from the stream
inlet = StreamInlet(streams[0])

while True:
        # get a new sample (you can also omit the timestamp part if you're not interested in it)
        chunk,timestamps = inlet.pull_chunk()
        if timestamps:
                print(chunk)

