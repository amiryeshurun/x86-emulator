# No support for XMM/YMM registers, yet
MAX_ALLOWED_READ_SIZE = 8
# Maximum page size in x86 is 0x1000
PAGE_SIZE = 0x1000
# Large page size, currently long-mode is supported
LARGE_PAGE_SIZE = 0x200000

DEFAULT_PG_ADDRESS = 0x1000