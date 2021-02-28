from enum import IntEnum

# No support for XMM/YMM registers, yet
MAX_ALLOWED_READ_SIZE = 8
# Maximum page size in x86 is 0x1000
PAGE_SIZE = 0x1000
# Large page size, currently long-mode is supported
TWO_MB_LARGE_PAGE_SIZE = 0x200000
# Default PML4 will reside in this address
DEFAULT_PG_ADDRESS = 0x1000
# Default address (physical address) for code
DEFAULT_CODE_ADDRESS = 0x2500

class PageTableEntryType(IntEnum):
    PTE = 0
    PDE = 1
    PDPTE = 2
    PML4E = 3