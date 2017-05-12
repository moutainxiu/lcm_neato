"""LCM type definitions
This file automatically generated by lcm.
DO NOT MODIFY BY HAND!!!!
"""

try:
    import cStringIO.StringIO as BytesIO
except ImportError:
    from io import BytesIO
import struct

class lidar_t(object):
    __slots__ = ["timestamp", "angle_min", "angle_max", "range_min", "range_max", "num_ranges", "ranges", "intensities"]

    def __init__(self):
        self.timestamp = 0
        self.angle_min = 0.0
        self.angle_max = 0.0
        self.range_min = 0
        self.range_max = 0
        self.num_ranges = 0
        self.ranges = []
        self.intensities = []

    def encode(self):
        buf = BytesIO()
        buf.write(lidar_t._get_packed_fingerprint())
        self._encode_one(buf)
        return buf.getvalue()

    def _encode_one(self, buf):
        buf.write(struct.pack(">qffiii", self.timestamp, self.angle_min, self.angle_max, self.range_min, self.range_max, self.num_ranges))
        buf.write(struct.pack('>%dh' % self.num_ranges, *self.ranges[:self.num_ranges]))
        buf.write(struct.pack('>%dh' % self.num_ranges, *self.intensities[:self.num_ranges]))

    def decode(data):
        if hasattr(data, 'read'):
            buf = data
        else:
            buf = BytesIO(data)
        if buf.read(8) != lidar_t._get_packed_fingerprint():
            raise ValueError("Decode error")
        return lidar_t._decode_one(buf)
    decode = staticmethod(decode)

    def _decode_one(buf):
        self = lidar_t()
        self.timestamp, self.angle_min, self.angle_max, self.range_min, self.range_max, self.num_ranges = struct.unpack(">qffiii", buf.read(28))
        self.ranges = struct.unpack('>%dh' % self.num_ranges, buf.read(self.num_ranges * 2))
        self.intensities = struct.unpack('>%dh' % self.num_ranges, buf.read(self.num_ranges * 2))
        return self
    _decode_one = staticmethod(_decode_one)

    _hash = None
    def _get_hash_recursive(parents):
        if lidar_t in parents: return 0
        tmphash = (0x1490b20baf5e38d) & 0xffffffffffffffff
        tmphash  = (((tmphash<<1)&0xffffffffffffffff)  + (tmphash>>63)) & 0xffffffffffffffff
        return tmphash
    _get_hash_recursive = staticmethod(_get_hash_recursive)
    _packed_fingerprint = None

    def _get_packed_fingerprint():
        if lidar_t._packed_fingerprint is None:
            lidar_t._packed_fingerprint = struct.pack(">Q", lidar_t._get_hash_recursive([]))
        return lidar_t._packed_fingerprint
    _get_packed_fingerprint = staticmethod(_get_packed_fingerprint)

