from enum import IntEnum
from bitarray import bitarray

class Segments(IntEnum):
    CS = 0
    DS = 1
    ES = 2
    SS = 3
    GS = 4
    FS = 5

class Selector:
    def __init__(self, value: int):
        self.set_new_value(value)
    
    def set_new_value(self, value: int):
        bit_array = bitarray(endian='little')
        bit_array.frombytes(value.to_bytes(2, 'little'))
        self.value = value
        self.rpl = int.from_bytes(bit_array[0:2].tobytes(), 'little')
        self.is_global = bit_array[2]
        self.index = int.from_bytes(bit_array[3:16].tobytes(), 'little')

NUM_SELECTORS = 6

class Selectors(IntEnum):
    SELECTOR_CS = 0
    SELECTOR_DS = 1
    SELECTOR_ES = 2
    SELECTOR_SS = 3
    SELECTOR_GS = 4
    SELECTOR_FS = 5

def segment_to_selector_index(segment: Segments) -> Selectors:
    return int(segment)