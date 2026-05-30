from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

class ZipPathValidator(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "dalvik/system/ZipPathValidator"
    clearCallback = JavaStaticMethod("()V")
    setCallback = JavaStaticMethod("(Ldalvik/system/ZipPathValidator$Callback;)V")

    class Callback(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "dalvik/system/ZipPathValidator$Callback"
        onZipEntryAccess = JavaMethod("(Ljava/lang/String;)V")

class DexClassLoader(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "dalvik/system/DexClassLoader"
    __javaconstructor__ = [("(Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;Ljava/lang/ClassLoader;)V", False)]

class PathClassLoader(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "dalvik/system/PathClassLoader"
    __javaconstructor__ = [("(Ljava/lang/String;Ljava/lang/ClassLoader;)V", False), ("(Ljava/lang/String;Ljava/lang/String;Ljava/lang/ClassLoader;)V", False)]

class DexFile(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "dalvik/system/DexFile"
    __javaconstructor__ = [("(Ljava/io/File;)V", False), ("(Ljava/lang/String;)V", False)]
    isDexOptNeeded = JavaStaticMethod("(Ljava/lang/String;)Z")
    loadDex = JavaStaticMethod("(Ljava/lang/String;Ljava/lang/String;I)Ldalvik/system/DexFile;")
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

class InMemoryDexClassLoader(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "dalvik/system/InMemoryDexClassLoader"
    __javaconstructor__ = [("(Ljava/nio/ByteBuffer;Ljava/lang/ClassLoader;)V", False), ("([Ljava/nio/ByteBuffer;Ljava/lang/ClassLoader;)V", False), ("([Ljava/nio/ByteBuffer;Ljava/lang/String;Ljava/lang/ClassLoader;)V", False)]

class ApplicationRuntime(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "dalvik/system/ApplicationRuntime"
    getBaseApkOptimizationInfo = JavaStaticMethod("()Ldalvik/system/DexFile$OptimizationInfo;")

class BaseDexClassLoader(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "dalvik/system/BaseDexClassLoader"
    __javaconstructor__ = [("(Ljava/lang/String;Ljava/io/File;Ljava/lang/String;Ljava/lang/ClassLoader;)V", False)]
    toString = JavaMethod("()Ljava/lang/String;")
    findLibrary = JavaMethod("(Ljava/lang/String;)Ljava/lang/String;")

class DelegateLastClassLoader(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "dalvik/system/DelegateLastClassLoader"
    __javaconstructor__ = [("(Ljava/lang/String;Ljava/lang/String;Ljava/lang/ClassLoader;Z)V", False), ("(Ljava/lang/String;Ljava/lang/String;Ljava/lang/ClassLoader;)V", False), ("(Ljava/lang/String;Ljava/lang/ClassLoader;)V", False)]
    getResource = JavaMethod("(Ljava/lang/String;)Ljava/net/URL;")
    getResources = JavaMethod("(Ljava/lang/String;)Ljava/util/Enumeration;")