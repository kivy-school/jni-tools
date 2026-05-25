from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["DexFile"]

class DexFile(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "dalvik/system/DexFile"
    __javaconstructor__ = [("(Ljava/io/File;)V", False), ("(Ljava/lang/String;)V", False)]
    loadDex = JavaStaticMethod("(Ljava/lang/String;Ljava/lang/String;I)Ldalvik/system/DexFile;")
    getName = JavaMethod("()Ljava/lang/String;")
    toString = JavaMethod("()Ljava/lang/String;")
    close = JavaMethod("()V")
    loadClass = JavaMethod("(Ljava/lang/String;Ljava/lang/ClassLoader;)Ljava/lang/Class;")
    entries = JavaMethod("()Ljava/util/Enumeration;")
    finalize = JavaMethod("()V")
    isDexOptNeeded = JavaStaticMethod("(Ljava/lang/String;)Z")

    class OptimizationInfo(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "dalvik/system/DexFile/OptimizationInfo"
        isVerified = JavaMethod("()Z")
        isOptimized = JavaMethod("()Z")
        isFullyCompiled = JavaMethod("()Z")