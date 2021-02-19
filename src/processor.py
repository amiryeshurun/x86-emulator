import ctl_regs
import mmu.x86_mem_constants
import mmu.paging
from mmu.memory import *
import msr

class Processor:
    def __init__(self, memory: Memory, id=0):
        self.id = id
        self.general_purpose_regs = []
        self.cr0 = ctl_regs.Cr0()
        self.cr2 = 0
        # Processor starts in real mode
        self.cr3 = 0
        self.msr = msr.Msr()
        # Paging is disabled, but we are preparing the mechanism for later
        self.paging = mmu.paging.Paging(memory)
    
    def is_long_mode_active(self) -> bool:
        return msr.EferMsr(self.msr[msr.MsrIndex.IA32_EFER]).long_mode_active
