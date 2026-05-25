from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["StructStatVfs"]

class StructStatVfs(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/system/StructStatVfs"
    __javaconstructor__ = [("(JJJJJJJJJJJ)V", False)]
    f_bavail = JavaField("J")
    f_bfree = JavaField("J")
    f_blocks = JavaField("J")
    f_bsize = JavaField("J")
    f_favail = JavaField("J")
    f_ffree = JavaField("J")
    f_files = JavaField("J")
    f_flag = JavaField("J")
    f_frsize = JavaField("J")
    f_fsid = JavaField("J")
    f_namemax = JavaField("J")
    toString = JavaMethod("()Ljava/lang/String;")