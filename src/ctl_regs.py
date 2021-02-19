from x86_exceptions import InvalidCr0Combination, AccessToReservedCr0Field
from bitarray import bitarray

class Cr0:
    DEFAULT_INITIAL_VALUE = 0x0

    def __init__(self):
        self.configuration = { 0 : "protected_mode", 1 : "monitor_co_processor", 2 : "emulation", \
                3: "task_switched", 4 : "extension_type", 5 : "numeric_error", 16 : "write_protect", \
                18 : "alignment_mask", 29 : "not_write_through", 30 : "cache_disable", 31 : "paging" }
        self.protected_mode = False
        self.monitor_co_processor = False
        self.emulation = False
        self.task_switched = False
        self.extension_type = False
        self.numeric_error = False
        self.write_protect = False
        self.alignment_mask = False
        self.not_write_through = False
        self.cache_disable = False
        self.paging = False
        self.value = DEFAULT_INITIAL_VALUE
    
    def validate_config(self, field_name: str, value: bool):
        current_value = getattr(self, field_name)
        if field_name == "protected_mode" and self.paging and not value:
            raise InvalidCr0Combination("Cannot exit PM while paging enabled")

    def change_configuration(self, idx: int, value: bool):
        try:
            field_name = self.configuration[idx]
        except:
            # Reserved fields
            if value != (self.value & (1 << idx)):
                raise AccessToReservedCr0Field(idx)
        validate_config(field_name, value)
        setattr(self, value)
    
    def get_field(self, idx: int) -> bool:
        try:
            field_name = self.configuration[idx]
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