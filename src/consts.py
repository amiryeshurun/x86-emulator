from enum import Enum

# No support for XMM/YMM registers, yet
MAX_ALLOWED_READ_SIZE = 8
PAGE_SIZE = 0x1000
LARGE_PAGE_SIZE = 0x200000

class Registers(Enum):
    REG_RAX = 0
    REG_RCX = 1
    REG_RDX = 2
    REG_RBX = 3
    REG_RSP = 4
    REG_RBP = 5
    REG_RSI = 6
    REG_RDI = 7
    REG_R8 = 8
    REG_R9 = 9
    REG_R10 = 10
    REG_R11 = 11
    REG_R12 = 12
    REG_R13 = 13
    REG_R14 = 14
    REG_R15 = 15
