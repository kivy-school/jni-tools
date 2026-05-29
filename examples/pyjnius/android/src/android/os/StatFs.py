from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["StatFs"]

class StatFs(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/os/StatFs"
    __javaconstructor__ = [("(Ljava/lang/String;)V", False)]
    getBlockCount = JavaMethod("()I")
    getTotalBytes = JavaMethod("()J")
    getFreeBytes = JavaMethod("()J")
    restat = JavaMethod("(Ljava/lang/String;)V")
    getBlockCountLong = JavaMethod("()J")
    getFreeBlocks = JavaMethod("()I")
    getAvailableBytes = JavaMethod("()J")
    getBlockSizeLong = JavaMethod("()J")
    getAvailableBlocks = JavaMethod("()I")
    getAvailableBlocksLong = JavaMethod("()J")
    getFreeBlocksLong = JavaMethod("()J")
    getBlockSize = JavaMethod("()I")