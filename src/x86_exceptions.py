"""
 This exception is thrown if the emulator tries to read a value bigger than
 the allowed maximum
"""
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
