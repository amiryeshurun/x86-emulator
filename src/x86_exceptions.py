"""
 This exception is thrown if the emulator tries to read a value bigger than
 the allowed maximum
"""
# For type-hinting
from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from processor import ProcessorMode

class InvalidReadSize(Exception):
    def __init__(self, size: int):
        self.offset = size
        self.message = f"Cannot read {size} bytes"
        super().__init__(self.message)

class AddressOutOfRange(Exception):
    def __init__(self, address: int, max_size: int):
        self.address = address
        self.message = f"Address {address} is out of range. Maximum address is {max_size}"
        super().__init__(self.message)

class InvalidCr0Combination(Exception):
    def __init__(self, msg: str):
        self.message = "Invalid Combination for CR0 ".append(msg)
        super().__init__(self.message)

class AccessToReservedCr0Field(Exception):
    def __init__(self, field: int):
        self.field = field
        self.message = f"Bit field at idx {field} is reserved and shall not be modified"
        super().__init__(self.message)

class InvalidMsrIndex(Exception):
    def __init__(self, idx: int):
        self.idx = idx
        self.message = f"Invalid MSR index: {idx}"
        super().__init__(self.message)

class AccessToReservedMsrIndex(Exception):
    def __init__(self, msr_idx: int, bit_field: int):
        self.msr_idx = msr_idx
        self.bit_field = bit_field
        self.message = f"Cannot change bit number {bit_field} of {msr_idx} MSR"
        super().__init__(self.message)

class InvalidEferCombination(Exception):
    def __init__(self, field_name: str, value: bool, ext: int):
        self.field_name = field_name
        self.value = value
        self.message = f"""Invalid combination for field {field_name}, value {value}. 
            Conflicts with: {ext:#0{4}x}"""

class InvalidEferAccess(Exception):
    def __init__(self, field_name: str, value: bool):
        self.message = f"Cannot change field {field_name} to {value}"
        super().__init__(self.message)

class PageFault(Exception):
    def __init__(self, is_minor: bool, virtual_address: int, address_length: int):
        self.is_minor = is_minor
        self.virtual_address = virtual_address
        pf_type_str = "minor" if is_minor else "major"
        self.message = f"A {pf_type_str} page-fault occured at {virtual_address:#0{address_length}x}"
        super().__init__(self.message)

class SegmentNotPresent(Exception):
    def __init__(self, segment: str):
        self.message = f"Segment {segment} is not present"
        super().__init__(self.message)

class InvalidProcessorMode(Exception):
    def __init__(self, mode: ProcessorMode):
        self.message = f"Unknown processor mode code: {int(mode)}"
        super().__init__(self.message)

class PriviledgeLevelNotAvailable:
    REASON_REAL_MODE = 0
    def __init__(self, reason: int):
        self.message = f"CPL is not accessible. Reason: "
        if reason == PriviledgeLevelNotAvailable.REASON_REAL_MODE:
            self.message.append("Priviledge level is not available when running in real-mode.")
        super().__init__(self.message)