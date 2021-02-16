import mmu.x86_mem_constants
from mmu.memory import *
import processor
from bitarray import bitarray

class PageTableEntry:
    def __init__(self, initial_value=0, pae=True):
        entry_size = 8 if pae else 4
        # We should create a new entry
        if initial_value == 0:
            pass
        # It is an existing entry
        else:
            bit_array = bitarray.frombytes(initial_value.to_bytes(entry_size, 'little'))

def setup_default_paging(proc: processor.Processor, memory: Memory):
    # First validate that paging is required
    if not proc.cr0.paging:
        return

def virtual_to_physical(proc: processor.Processor, memory: Memory, virtual_address: int) -> int:
    pass
