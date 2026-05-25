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
    def __init__(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: int, arg10: int) -> None: ...
    def toString(self) -> str: ...
