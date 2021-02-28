# For type-hinting
from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from processor import Processor
from x86_exceptions import Unimplemented
from instructions.instruction import *

def decode_16(proc: Processor):
    pass

def decode_32(proc: Processor):
    raise Unimplemented

def decode_64(proc: Processor):
    raise Unimplemented