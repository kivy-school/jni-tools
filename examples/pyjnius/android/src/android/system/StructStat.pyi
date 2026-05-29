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
    def __init__(self, p0: int, p1: int, p2: int, p3: int, p4: int, p5: int, p6: int, p7: int, p8: StructTimespec, p9: StructTimespec, p10: StructTimespec, p11: int, p12: int) -> None: ...
    @overload
    def __init__(self, p0: int, p1: int, p2: int, p3: int, p4: int, p5: int, p6: int, p7: int, p8: int, p9: int, p10: int, p11: int, p12: int) -> None: ...
    def toString(self) -> str: ...
