from x86_exceptions import InvalidPageOffset, InvalidPageReadSize
import consts

class Page:
    def __init__(self, large_page=False):
        self.page_data = bytearray()
        self.large_page = large_page
    
    def get_mem_at_offset(self, offset: int, size: int):
        # First, validate read size
        if size > MAX_ALLOWED_READ_SIZE:
            raise InvalidPageReadSize(size)
        if self.large_page:
            if offset > LARGE_PAGE_SIZE:
                raise InvalidPageOffset(offset, True)
        else:
            if offset > PAGE_SIZE:
                raise InvalidPageOffset(offset, False)
        return self.page_data[offset, offset + size]


        