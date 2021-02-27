import ctl_regs
import msr
import mmu.x86_mem_constants
import mmu.paging
import segmentation.gdt
import segmentation.selectors
from enum import IntEnum
from x86_exceptions import InvalidProcessorMode, PriviledgeLevelNotAvailable
from mmu.memory import *

class ProcessorMode(IntEnum):
    REAL_MODE = 0
    PROTECTED_MODE = 1
    COMPATIBILITY_MODE = 2
    LONG_MODE = 3

class Processor:
    def __init__(self, memory: Memory, initial_mode=ProcessorMode.REAL_MODE, id=0):
        self.id = id
        self.general_purpose_regs = []
        self.memory = memory
        # Paging might be disabled, but we are preparing the mechanism for later
        self.paging = mmu.paging.Paging(memory)

        # Check the initial processor mode
        if initial_mode == ProcessorMode.REAL_MODE:
            self.setup_real_mode()
        elif initial_mode == ProcessorMode.PROTECTED_MODE:
            pass
        elif initial_mode == ProcessorMode.COMPATIBILITY_MODE:
            pass
        elif initial_mode == ProcessorMode.LONG_MODE:
            pass
        else:
            raise InvalidProcessorMode(initial_mode)
    
    def setup_real_mode(self):
        self.cr0 = ctl_regs.Cr0()
        self.cr2 = 0
        # Real mode, CR3 is cleared to 0
        self.cr3 = 0
        self.msr = msr.Msr()
        # GDT & Selectors
        self.selectors = segmentation.selectors.NUM_SELECTORS * [segmentation.selectors.Selector(0)]
        self.gdt = segmentation.gdt.Gdt()

    def is_in_real_mode(self) -> bool:
        return not self.cr0.protected_mode

    def is_long_mode_active(self) -> bool:
        return msr.EferMsr(self, self.msr[msr.MsrIndex.IA32_EFER]).long_mode_active

    def get_current_cpl(self) -> int:
        if self.is_in_real_mode():
            raise PriviledgeLevelNotAvailable(PriviledgeLevelNotAvailable.REASON_REAL_MODE)
        return self.selectors[segmentation.selectors.Selectors.SELECTOR_CS].rpl