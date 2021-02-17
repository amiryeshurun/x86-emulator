import ctl_regs
import mmu.x86_mem_constants
import mmu.paging
from mmu.memory import *

class Processor:
    def __init__(self, memory: Memory, id=0):
        self.id = id
        self.general_purpose_regs = []
        self.cr0 = ctl_regs.Cr0()
        mmu.paging.setup_default_paging(self)
