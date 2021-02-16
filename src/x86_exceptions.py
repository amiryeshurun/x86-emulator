"""
 This exception is thrown if the emulator tries to access an invalid page
 offset within a page (1KB for regualr pages, 2MB for large pages)
"""
class InvalidPageOffset(Exception):
    def __init__(self, offset: int, large_page=False):
        self.offset = offset
        self.large_page = large_page
        if large_page:
            self.message = f"Invalid offset {offset} for a large page"
        else:
            self.message = f"Invalid offset {offset} for a regular page"
        super().__init__(self.message)


"""
 This exception is thrown if the emulator tries to read a value higher than
 the allowed maximum
"""
class InvalidPageReadSize(Exception):
    def __init__(self, size: int):
        self.offset = size
        self.message = f"Cannot read {size} bytes"
        super().__init__(self.message)