# For type-hinting
from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from processor import Processor
import abc
from enum import IntEnum
from typing import Type, Dict
from x86_exceptions import InvalidOpcode, InvalidInstructionCode

class InstructionCodes(IntEnum):
    MOV_RM8_R8 = 0

    @classmethod
    def has_value(cls, value: InstructionCodes):
        return value in set(item.value for item in InstructionCodes)

class Opcodes(IntEnum):
    MOV_RM8_R8 = 0x88
    
    @classmethod
    def has_value(cls, value: Opcodes):
        return value in set(item.value for item in Opcodes)
        
opcode_to_instruction_code: Dict[Opcodes, InstructionCodes] = {}

def register_opcode(opcode: Opcodes, instruction_code: InstructionCodes):
    global opcode_to_instruction_code
    
    # First make sure that the opcode exists
    if not Opcodes.has_value(opcode):
        raise InvalidOpcode(opcode)
    # If so, save it
    opcode_to_instruction_code[opcode] = instruction_code

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

instruction_code_to_instruction_object: Dict[InstructionCodes, Instruction] = {}

def register_instruction(instruction_code: InstructionCodes, instruction_object: Type[Instruction]):
    global instruction_code_to_instruction_object
    
    # First make sure that the opcode exists
    if not InstructionCodes.has_value(instruction_code):
        raise InvalidInstructionCode(instruction_code)
    # If so, save it
    instruction_code_to_instruction_object[instruction_code] = instruction_object()

