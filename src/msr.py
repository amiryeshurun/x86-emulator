from enum import Enum
from x86_exceptions import InvalidMsrIndex, AccessToReservedMsrIndex, InvalidEferAccess
from bitarray import bitarray
import processor

class MsrIndex(Enum):
    FIRST_RANGE_START = 0
    FIRST_RANGE_MAX = 0x1fff
    SECOND_RANGE_START = 0xc0000000
    SECOND_RANGE_MAX = 0xc0001fff

    IA32_EFER = 0xc0000080

class EferMsr:
    DEFAULT_INITIAL_VALUE = 0x1
    configuration = { 0 : "system_call_extension", 1 : "data_fetch_enabled", 4 : "l2_cache_disabled", \
                8: "long_mode_enabled", 10 : "long_mode_active", 11 : "no_execute_enabled", \
                13 : "long_mode_segment_limit_enabled" }
    
    def __init__(self, value=DEFAULT_INITIAL_VALUE):
        bit_array = bitarray(endian='little')
        bit_array.frombytes(value.to_bytes(4, 'little'))
        self.system_call_extension = bit_array[0]
        self.data_fetch_enabled = bit_array[1]
        self.l2_cache_disabled = bit_array[4]
        self.long_mode_enabled = bit_array[8]
        self.long_mode_active = bit_array[10]
        self.no_execute_enabled = bit_array[11]
        self.long_mode_segment_limit_enabled = bit_array[13]
        self.value = value

    def validate_config(self, field_name: str, value: bool):
        current_value = getattr(self, field_name)
        if field_name == "long_mode_active" and value != self.long_mode_active:
            raise InvalidEferAccess(field_name, value)

    def change_configuration(self, idx: int, value: bool):
        try:
            field = configuration[idx]
        except:
            # Reserved fields
            if value != (self.value & (1 << idx)):
                raise AccessToReservedMsrIndex(MsrIndex.IA32_EFER, idx)
        self.validate_config(field, value)
        setattr(self, field, value)

    def get_field(self, idx: int) -> bool:
        try:
            field = configuration[idx]
        except:
            return False
        return getattr(self, field_name) 

    def set_value(self, value: int):
        bit_array = bitarray(endian='little')
        bit_array.frombytes(value.to_bytes(4, 'little'))
        for i in range(0, len(bit_array)):
            self.change_configuration(i, bit_array[i])
        self.value = value
    
    def get_value(self) -> int:
        return self.value

class Msr:
    def __init__(self):
        # Allocate MSR ranges
        self.msr_first_range = 0x1fff * [None]
        self.msr_second_range = 0x1fff * [None]
        # Create the actual MSR values
        self.msr_first_range[MsrIndex.IA32_EFER] = EferMsr.DEFAULT_INITIAL_VALUE
    
    def __getitem__(self, key):
        if MsrIndex.FIRST_RANGE_START <= key <= MsrIndex.FIRST_RANGE_MAX:
            return self.msr_first_range[key]
        elif MsrIndex.SECOND_RANGE_START <= key <= MsrIndex.SECOND_RANGE_MAX:
            return self.msr_second_range[key]
        raise InvalidMsrIndex(idx)
    
    def __setitem__(self, key, value):
        if MsrIndex.FIRST_RANGE_START <= key <= MsrIndex.FIRST_RANGE_MAX:
            self.msr_first_range[key] = value
        elif MsrIndex.SECOND_RANGE_START <= key <= MsrIndex.SECOND_RANGE_MAX:
            self.msr_second_range[key] = value
        else:
            raise InvalidMsrIndex(idx)

        