import consts

def is_page_aligned(address: int) -> bool:
    return True if address % PAGE_SIZE == 0 else False
