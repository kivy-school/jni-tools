from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["StructStat"]

class StructStat(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/system/StructStat"
    __javaconstructor__ = [("(JJIJIIJJLandroid/system/StructTimespec;Landroid/system/StructTimespec;Landroid/system/StructTimespec;JJ)V", False), ("(JJIJIIJJJJJJJ)V", False)]
    st_atim = JavaField("Landroid/system/StructTimespec;")
    st_atime = JavaField("J")
    st_blksize = JavaField("J")
    st_blocks = JavaField("J")
    st_ctim = JavaField("Landroid/system/StructTimespec;")
    st_ctime = JavaField("J")
    st_dev = JavaField("J")
    st_gid = JavaField("I")
    st_ino = JavaField("J")
    st_mode = JavaField("I")
    st_mtim = JavaField("Landroid/system/StructTimespec;")
    st_mtime = JavaField("J")
    st_nlink = JavaField("J")
    st_rdev = JavaField("J")
    st_size = JavaField("J")
    st_uid = JavaField("I")
    toString = JavaMethod("()Ljava/lang/String;")