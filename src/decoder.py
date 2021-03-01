# For type-hinting
from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from processor import Processor
from x86_exceptions import Unimplemented, UnorderedPrefixList
from instructions.instruction import *
from bitarray import bitarray
from enum import IntEnum
from segmentation.selectors import Segments

def check_for_prefix(instruction: bytearray):
    prefix = int(instruction[0])

    if FirstGroupPrefix.has_value(prefix):
        return PrefixTypes.FIRST, prefix
    elif SecondGroupPrefix.has_value(prefix):
        return PrefixTypes.FIRST, prefix
    elif ThirdGroupPrefix.has_value(prefix):
        return PrefixTypes.SECOND, prefix
    elif FourthGroupPrefix.has_value(prefix):
        return PrefixTypes.FOURTH, prefix
    
    return PrefixTypes.NONE, prefix

def decode_16(proc: Processor):
    instruction_address = proc.get_current_instruction_address()
    offset_from_beginning = 0
    instruction_size = 1
    instruction = proc.read_memory(instruction_address, 1, Segments.CS)
    prefix_list = []
    # First check if there is an instruction prefix
    while True:
        prefix_type, prefix = check_for_prefix(instruction)
        if prefix_type != PrefixTypes.NONE:
            # Check if the prefixes are ordered
            if len(prefix_list) > 0 and prefix_list[-1][0] > prefix_type:
                raise UnorderedPrefixList(prefix_list[-1][0], prefix_type)
            # Add to list of prefixes
            prefix_list.append([prefix_type, prefix])
            # Next byte
            offset_from_beginning += 1
            # Increment size
            instruction_size += 1
            # Read next byte
            instruction = proc.read_memory(instruction_address + offset_from_beginning,
            1, Segments.CS)
        else:
            break
    # Now 'instruction' contains the first byte of the opcode

def decode_32(proc: Processor):
    raise Unimplemented

def decode_64(proc: Processor):
    raise Unimplemented