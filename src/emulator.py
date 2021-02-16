from x86_mem_constants import *
from processor import *
from memory import *
import paging

class Emulator:
    def __init__(self, cpu_count=1, physical_memory_size=LARGE_PAGE_SIZE):
        self.processors = []
        self.memory = Memory(physical_memory_size)
        for i in range(0, cpu_count):
            self.processors.append(Processor(memory, id=i))

