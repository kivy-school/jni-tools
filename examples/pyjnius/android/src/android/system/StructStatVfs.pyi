from typing import Any, ClassVar, overload

class StructStatVfs:
    f_bavail: int
    f_bfree: int
    f_blocks: int
    f_bsize: int
    f_favail: int
    f_ffree: int
    f_files: int
    f_flag: int
    f_frsize: int
    f_fsid: int
    f_namemax: int
    def __init__(self, p0: int, p1: int, p2: int, p3: int, p4: int, p5: int, p6: int, p7: int, p8: int, p9: int, p10: int) -> None: ...
    def toString(self) -> str: ...
