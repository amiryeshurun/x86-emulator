# For type-hinting
from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from processor import Processor
from x86_exceptions import SegmentNotPresent

class Gdt:
    def __init__(self):
        self.address = None
    
    def load_gdt(self, proc: Processor, operand: int):
        pass

