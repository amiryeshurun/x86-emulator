# For type-hinting
from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from processor import Processor
import abc
from enum import IntEnum
from typing import Type, Dict
from x86_exceptions import InvalidOpcode, InvalidInstructionCode

X86_OPCODE_EXPANSION = 0xF0

class InstructionCodes(IntEnum):
    MOV_RM8_R8 = 0
    ADD_RM8_R8 = 1

    @classmethod
    def has_value(cls, value: InstructionCodes):
        return value in set(item.value for item in InstructionCodes)

class Opcodes(IntEnum):
    ADD_RM8_R8 = 0x0
    MOV_RM8_R8 = 0x88
    
    @classmethod
    def has_value(cls, value: Opcodes):
        return value in set(item.value for item in Opcodes)
        
opcode_to_instruction_code: Dict[Opcodes, InstructionCodes] = {}
instruction_code_to_instruction_object: Dict[InstructionCodes, Instruction] = {}

def register_opcode(opcode: Opcodes, instruction_code: InstructionCodes):
    global opcode_to_instruction_code
    
    # First make sure that the opcode exists
    if not Opcodes.has_value(opcode):
        raise InvalidOpcode(opcode)
    # If so, save it
    opcode_to_instruction_code[opcode] = instruction_code

def register_instruction(instruction_code: InstructionCodes, instruction_object: Type[Instruction]):
    global instruction_code_to_instruction_object
    
    # First make sure that the opcode exists
    if not InstructionCodes.has_value(instruction_code):
        raise InvalidInstructionCode(instruction_code)
    # If so, save it
    instruction_code_to_instruction_object[instruction_code] = instruction_object()

class PrefixTypes(IntEnum):
    FIRST = 0
    SECOND = 1
    THIRD = 2
    FOURTH = 4
    NONE = 5

class FirstGroupPrefix(IntEnum):
    LOCK = 0xF0
    REPNZ = 0xF2
    REPNE = 0xF2
    REP = 0xF3
    BND = 0xF2

    @classmethod
    def has_value(cls, value: FirstGroupPrefix):
        return value in set(item.value for item in FirstGroupPrefix)

class SecondGroupPrefix(IntEnum):
    CS_OVERRIDE = 0x2E
    SS_OVERRIDE = 0x36
    DS_OVERRIDE = 0x3E
    ES_OVERRIDE = 0x26
    FS_OVERRIDE = 0x64
    GD_OVERRIDE = 0x65
    BRANCH_NOT_TAKEN = 0x2E
    BRANCH_TAKEN = 0x3E

    @classmethod
    def has_value(cls, value: SecondGroupPrefix):
        return value in set(item.value for item in SecondGroupPrefix)
    
class ThirdGroupPrefix(IntEnum):
    OPERAND_SIZE_OVERRIDE = 0x66

    @classmethod
    def has_value(cls, value: ThirdGroupPrefix):
        return value in set(item.value for item in ThirdGroupPrefix)

class FourthGroupPrefix(IntEnum):
    ADDRESS_SIZE_OVERRIDE = 0x67

    @classmethod
    def has_value(cls, value: FourthGroupPrefix):
        return value in set(item.value for item in FourthGroupPrefix)

class Instruction(metaclass=abc.ABCMeta):
    @classmethod
    def __subclasshook__(cls, subclass):
        return (hasattr(subclass, 'parse_arguments') and 
                callable(subclass.parse_arguments) and 
                hasattr(subclass, 'execute') and 
                callable(subclass.execute))

    @abc.abstractmethod
    def parse_arguments(self, inst: bytearray) -> list:
        raise NotImplementedError

    @abc.abstractmethod
    def execute(self, proc: Processor, args: list):
        raise NotImplementedError

