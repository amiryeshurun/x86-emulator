from enum import IntEnum
from bitarray import bitarray

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
    SELECTOR_DS = 0
    SELECTOR_ES = 0
    SELECTOR_SS = 0
    SELECTOR_GS = 0
    SELECTOR_FS = 0