from enum import IntEnum

class Instructions(IntEnum):
    MOV_R8_RM8 = 0

class Opcodes(IntEnum):
    MOV_R8_RM8 = 0x88

opcode_to_instruction_code = {}
opcode_to_instruction_code[Opcodes.MOV_R8_RM8] = Instructions.MOV_R8_RM8