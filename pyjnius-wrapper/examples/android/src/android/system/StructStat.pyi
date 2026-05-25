from typing import Any, ClassVar, overload
from android.system.StructTimespec import StructTimespec

class StructStat:
    st_atim: StructTimespec
    st_atime: int
    st_blksize: int
    st_blocks: int
    st_ctim: StructTimespec
    st_ctime: int
    st_dev: int
    st_gid: int
    st_ino: int
    st_mode: int
    st_mtim: StructTimespec
    st_mtime: int
    st_nlink: int
    st_rdev: int
    st_size: int
    st_uid: int
    @overload
    def __init__(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: int, arg10: int, arg11: int, arg12: int) -> None: ...
    @overload
    def __init__(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: StructTimespec, arg9: StructTimespec, arg10: StructTimespec, arg11: int, arg12: int) -> None: ...
    def toString(self) -> str: ...
