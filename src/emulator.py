import mmu.paging
from mmu.x86_mem_constants import *
from processor import *
from mmu.memory import *

# Import all instructions in order to perform initialization
import instructions.mov

class Emulator:
    def __init__(
        self, cpu_count=1, initial_mode=ProcessorMode.REAL_MODE, 
        code_begin_address=DEFAULT_CODE_ADDRESS, physical_memory_size=TWO_MB_LARGE_PAGE_SIZE
        ):
        self.processors = []
        self.memory = Memory(physical_memory_size)
        for i in range(0, cpu_count):
            self.processors.append(Processor(self.memory, id=i, initial_mode=initial_mode))

    def load_code_to_memory(self, code: bytearray, physical_address=DEFAULT_CODE_ADDRESS):
        self.memory.write_physical_mem(physical_address, code)

    def start_execution(self):
        self.processors[0].start_execution()
        
