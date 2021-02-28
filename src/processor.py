import ctl_regs
import msr
import decoder
import mmu.x86_mem_constants
import mmu.paging
import segmentation.gdt
import segmentation.selectors
import instructions.instruction
from enum import IntEnum
from x86_exceptions import InvalidProcessorMode, PriviledgeLevelNotAvailable, Unimplemented
from mmu.memory import *

class ProcessorMode(IntEnum):
    REAL_MODE = 0
    PROTECTED_MODE = 1
    COMPATIBILITY_MODE = 2
    LONG_MODE = 3

class ExecutionMode(IntEnum):
    EXEC_16 = 0
    EXEC_32 = 1
    EXEC_64 = 2

class Processor:
    def __init__(
        self, memory: Memory, initial_mode=ProcessorMode.REAL_MODE, 
        start_rip=DEFAULT_CODE_ADDRESS, id=0
        ):
        self.id = id
        self.general_purpose_regs = GP_REGISTERS_COUNT * [0]
        self.memory = memory
        # Paging might be disabled, but we are preparing the mechanism for later
        self.paging = mmu.paging.Paging(memory)
        self.rip = DEFAULT_CODE_ADDRESS

        # Check the initial processor mode
        if initial_mode == ProcessorMode.REAL_MODE:
            self.setup_real_mode()
        elif initial_mode == ProcessorMode.PROTECTED_MODE:
            raise Unimplemented
        elif initial_mode == ProcessorMode.COMPATIBILITY_MODE:
            raise Unimplemented
        elif initial_mode == ProcessorMode.LONG_MODE:
            raise Unimplemented
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
        self.current_mode = ProcessorMode.REAL_MODE
        
    def is_in_real_mode(self) -> bool:
        return not self.cr0.protected_mode

    def is_long_mode_active(self) -> bool:
        return msr.EferMsr(self, self.msr[msr.MsrIndex.IA32_EFER]).long_mode_active

    def get_current_cpl(self) -> int:
        if self.is_in_real_mode():
            raise PriviledgeLevelNotAvailable(PriviledgeLevelNotAvailable.REASON_REAL_MODE)
        return self.selectors[segmentation.selectors.Selectors.SELECTOR_CS].rpl
    
    def update_execution_mode(self):
        if self.is_in_real_mode():
            self.current_mode = ProcessorMode.REAL_MODE
        # Currently unimplemented
        raise Unimplemented
        # When the processor is running in protected mode, we should check the code segment selector
        if not self.selectors[segmentation.selectors.Selectors.SELECTOR_CS].is_global:
            raise Unimplemented
    
    def get_instruction_mode(self) -> ExecutionMode:
        if self.current_mode == ProcessorMode.REAL_MODE:
            return ExecutionMode.EXEC_16
        # Currently unimplemented
        raise Unimplemented

    def start_execution(self):
        exec_mode_to_decoder = {
            ExecutionMode.EXEC_16 : decoder.decode_16
            ExecutionMode.EXEC_32 : decoder.decode_32
            ExecutionMode.EXEC_64 : decoder.decode_64
        }
        while True:
            try:
                self.update_execution_mode()
                exec_mode = self.get_instruction_mode()
                # The decoder returns an instruction code and a list of arguments
                inst_code, args = exec_mode_to_decoder[exec_mode](self)
                # Execute the instruction
                instructions.instruction.instruction_code_to_instruction_object[inst_code]
                .execute(self, args)
            except:
                print('ERR')
       
            