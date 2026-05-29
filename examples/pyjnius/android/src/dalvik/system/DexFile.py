from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["DexFile"]

class DexFile(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "dalvik/system/DexFile"
    __javaconstructor__ = [("(Ljava/io/File;)V", False), ("(Ljava/lang/String;)V", False)]
    loadDex = JavaStaticMethod("(Ljava/lang/String;Ljava/lang/String;I)Ldalvik/system/DexFile;")
    isDexOptNeeded = JavaStaticMethod("(Ljava/lang/String;)Z")
    getName = JavaMethod("()Ljava/lang/String;")
    loadClass = JavaMethod("(Ljava/lang/String;Ljava/lang/ClassLoader;)Ljava/lang/Class;")
    toString = JavaMethod("()Ljava/lang/String;")
    close = JavaMethod("()V")
    entries = JavaMethod("()Ljava/util/Enumeration;")

    class OptimizationInfo(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "dalvik/system/DexFile$OptimizationInfo"
        isOptimized = JavaMethod("()Z")
        isVerified = JavaMethod("()Z")
        isFullyCompiled = JavaMethod("()Z")