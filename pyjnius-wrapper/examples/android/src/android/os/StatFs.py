from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["StatFs"]

class StatFs(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/os/StatFs"
    __javaconstructor__ = [("(Ljava/lang/String;)V", False)]
    restat = JavaMethod("(Ljava/lang/String;)V")
    getBlockSize = JavaMethod("()I")
    getBlockSizeLong = JavaMethod("()J")
    getBlockCount = JavaMethod("()I")
    getBlockCountLong = JavaMethod("()J")
    getFreeBlocks = JavaMethod("()I")
    getFreeBlocksLong = JavaMethod("()J")
    getFreeBytes = JavaMethod("()J")
    getAvailableBlocks = JavaMethod("()I")
    getAvailableBlocksLong = JavaMethod("()J")
    getAvailableBytes = JavaMethod("()J")
    getTotalBytes = JavaMethod("()J")