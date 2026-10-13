import serial, struct
import matplotlib.pyplot as plt

PORT = "COM11"  # your port
s = serial.Serial(PORT, 115200, timeout=0.1)
buf, pts = bytearray(), {}
plt.ion()
ax = plt.figure().add_subplot(111, projection="polar")

while plt.fignum_exists(1):
    buf += s.read(1024)
    while True:
        i = buf.find(b"\x55\xAA\x02\x08")
        if i < 0 or len(buf) < i + 28:
            if i > 0: del buf[:i]
            break
        pkt = bytes(buf[i:i+28]); del buf[:i+28]
        start, end = struct.unpack_from("<H", pkt, 6)[0], struct.unpack_from("<H", pkt, 24)[0]
        a0, a1 = (start - 0xA000) / 64, (end - 0xA000) / 64
        if a1 < a0: a1 += 360
        for k, d in enumerate(struct.unpack_from("<8H", pkt, 8)):
            deg = round((a0 + k * (a1 - a0) / 7) % 360)
            if d == 0x8000: pts.pop(deg, None)
            else: pts[deg] = d
    ax.cla()
    ax.set_ylim(0, 2000)          # fixed radius range in mm (0 to 3 m)
    ax.set_yticks([500, 1000, 1500, 2000])
    ax.scatter([a * 3.14159 / 180 for a in pts], list(pts.values()), s=4)
    plt.pause(0.05)
    plt.pause(0.05)