from processor import Processor
from instructions.instruction import *

class MovRm8R8(Instruction):
    def parse_arguments(self, inst: bytearray) -> list:
        raise NotImplementedError
    
    def execute(self, proc: Processor, args: list):
        raise NotImplementedError

# Register all opcodes
register_opcode(Opcodes.MOV_RM8_R8, InstructionCodes.MOV_RM8_R8)

register_instruction(InstructionCodes.MOV_RM8_R8, MovRm8R8)