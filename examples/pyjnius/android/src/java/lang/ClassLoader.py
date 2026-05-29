from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ClassLoader"]

class ClassLoader(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/lang/ClassLoader"
    getName = JavaMethod("()Ljava/lang/String;")
    loadClass = JavaMethod("(Ljava/lang/String;)Ljava/lang/Class;")
    getPlatformClassLoader = JavaStaticMethod("()Ljava/lang/ClassLoader;")
    getSystemClassLoader = JavaStaticMethod("()Ljava/lang/ClassLoader;")
    getSystemResourceAsStream = JavaStaticMethod("(Ljava/lang/String;)Ljava/io/InputStream;")
    getResourceAsStream = JavaMethod("(Ljava/lang/String;)Ljava/io/InputStream;")
    getSystemResource = JavaStaticMethod("(Ljava/lang/String;)Ljava/net/URL;")
    getResource = JavaMethod("(Ljava/lang/String;)Ljava/net/URL;")
    getResources = JavaMethod("(Ljava/lang/String;)Ljava/util/Enumeration;")
    getDefinedPackage = JavaMethod("(Ljava/lang/String;)Ljava/lang/Package;")
    resources = JavaMethod("(Ljava/lang/String;)Ljava/util/stream/Stream;")
    isRegisteredAsParallelCapable = JavaMethod("()Z")
    getSystemResources = JavaStaticMethod("(Ljava/lang/String;)Ljava/util/Enumeration;")
    getParent = JavaMethod("()Ljava/lang/ClassLoader;")
    getUnnamedModule = JavaMethod("()Ljava/lang/Module;")
    getDefinedPackages = JavaMethod("()[Ljava/lang/Package;")
    setDefaultAssertionStatus = JavaMethod("(Z)V")
    setPackageAssertionStatus = JavaMethod("(Ljava/lang/String;Z)V")
    setClassAssertionStatus = JavaMethod("(Ljava/lang/String;Z)V")
    clearAssertionStatus = JavaMethod("()V")