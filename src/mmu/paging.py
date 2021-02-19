from mmu.x86_mem_constants import *
from mmu.memory import *
from processor import *
from bitarray import bitarray

class PageTableEntry:
    def __init__(self, page_type: PageTableEntryType, initial_value=0, pae=True):
        entry_size = 8 if pae else 4
        # We should create a new entry
        if initial_value == 0:
            pass
        # It is an existing entry
        else:
            bit_array = bitarray(endian='little')
            bit_array.frombytes(initial_value.to_bytes(entry_size, 'little'))
            self.parse_config_bytes(bit_array, page_type)

    def parse_config_bytes(self, bit_array: bitarray, page_type: PageTableEntryType):
        self.present = bit_array[0]
        self.read_write = bit_array[1]
        self.user = bit_array[2]
        self.write_through = bit_array[3]
        self.cache_disabled = bit_array[4]
        self.accessed = bit_array[5]
        if page_type == PageTableEntryType.PTE:
            self.dirty = bit_array[6]
            self.glob = bit_array[8]
        if page_type in [PageTableEntryType.PDE, PageTableEntryType.PDPTE]:
            self.large_page = bit_array[7]
        self.address = int.from_bytes(bit_array[12:].tobytes(), 'little') << 12

class Paging:
    def __init__(self, memory: Memory):
        self.global_memory = memory
    
    def virtual_to_physical(proc: Processor, virtual_address: int) -> int:
        

    def get_memory(proc: Processor, virtual_address: int, length: int) -> bytearray:
        
