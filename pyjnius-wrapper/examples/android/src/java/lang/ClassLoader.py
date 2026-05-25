from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ClassLoader"]

class ClassLoader(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/lang/ClassLoader"
    __javaconstructor__ = [("(Ljava/lang/ClassLoader;)V", False), ("()V", False)]
    loadClass = JavaMultipleMethod([("(Ljava/lang/String;)Ljava/lang/Class;", False, False), ("(Ljava/lang/String;Z)Ljava/lang/Class;", False, False)])
    findClass = JavaMethod("(Ljava/lang/String;)Ljava/lang/Class;")
    defineClass = JavaMultipleMethod([("([BII)Ljava/lang/Class;", False, False), ("(Ljava/lang/String;[BII)Ljava/lang/Class;", False, False), ("(Ljava/lang/String;[BIILjava/security/ProtectionDomain;)Ljava/lang/Class;", False, False), ("(Ljava/lang/String;Ljava/nio/ByteBuffer;Ljava/security/ProtectionDomain;)Ljava/lang/Class;", False, False)])
    resolveClass = JavaMethod("(Ljava/lang/Class;)V")
    findSystemClass = JavaMethod("(Ljava/lang/String;)Ljava/lang/Class;")
    findLoadedClass = JavaMethod("(Ljava/lang/String;)Ljava/lang/Class;")
    setSigners = JavaMethod("(Ljava/lang/Class;[Ljava/lang/Object;)V")
    getResource = JavaMethod("(Ljava/lang/String;)Ljava/net/URL;")
    getResources = JavaMethod("(Ljava/lang/String;)Ljava/util/Enumeration;")
    findResource = JavaMethod("(Ljava/lang/String;)Ljava/net/URL;")
    findResources = JavaMethod("(Ljava/lang/String;)Ljava/util/Enumeration;")
    registerAsParallelCapable = JavaStaticMethod("()Z")
    getSystemResource = JavaStaticMethod("(Ljava/lang/String;)Ljava/net/URL;")
    getSystemResources = JavaStaticMethod("(Ljava/lang/String;)Ljava/util/Enumeration;")
    getResourceAsStream = JavaMethod("(Ljava/lang/String;)Ljava/io/InputStream;")
    getSystemResourceAsStream = JavaStaticMethod("(Ljava/lang/String;)Ljava/io/InputStream;")
    getParent = JavaMethod("()Ljava/lang/ClassLoader;")
    getSystemClassLoader = JavaStaticMethod("()Ljava/lang/ClassLoader;")
    definePackage = JavaMethod("(Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;Ljava/net/URL;)Ljava/lang/Package;")
    getPackage = JavaMethod("(Ljava/lang/String;)Ljava/lang/Package;")
    getPackages = JavaMethod("()[Ljava/lang/Package;")
    findLibrary = JavaMethod("(Ljava/lang/String;)Ljava/lang/String;")
    setDefaultAssertionStatus = JavaMethod("(Z)V")
    setPackageAssertionStatus = JavaMethod("(Ljava/lang/String;Z)V")
    setClassAssertionStatus = JavaMethod("(Ljava/lang/String;Z)V")
    clearAssertionStatus = JavaMethod("()V")