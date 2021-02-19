import mmu.paging
from mmu.x86_mem_constants import *
from processor import *
from mmu.memory import *


class Emulator:
    def __init__(self, cpu_count=1, physical_memory_size=TWO_MB_LARGE_PAGE_SIZE):
        self.processors = []
        self.memory = mmu.memory.Memory(physical_memory_size)
        for i in range(0, cpu_count):
            self.processors.append(Processor(self.memory, id=i))

