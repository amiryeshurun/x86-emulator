from mmu.x86_mem_constants import *
from x86_exceptions import AddressOutOfRange

class Memory:
    def __init__(self, fixed_size=LARGE_PAGE_SIZE):
        self.size = fixed_size
        self.physical_memory = bytearray(fixed_size)
    
    def read_physical_mem(self, begin: int, read_length: int) -> bytearray:
        if begin >= self.size or (begin + read_length) >= self.size:
            raise AddressOutOfRange(begin, self.size)
        return self.physical_memory[begin : begin + read_length]
    
    def write_physical_mem(self, address: int, data: bytearray):
        if address >= self.size or (address + len(data)) >= self.size:
            raise AddressOutOfRange(address, self.size)
        self.physical_memory[address : address + len(data)] = data

