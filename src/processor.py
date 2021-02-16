import mmu.x86_mem_constants
import mmu.paging
from mmu.memory import *
import ctl_regs

class Processor:
    def __init__(self, memory: Memory, id=0):
        self.id = id
        self.general_purpose_regs = []
        self.cr0 = ctl_regs.Cr0()
        mmu.paging.setup_default_paging(self)

mmu.paging.PageTableEntry(0x1003)