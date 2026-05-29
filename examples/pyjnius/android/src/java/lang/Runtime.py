from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Runtime"]

class Runtime(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/lang/Runtime"
    getRuntime = JavaStaticMethod("()Ljava/lang/Runtime;")
    exit = JavaMethod("(I)V")
    runFinalization = JavaMethod("()V")
    version = JavaStaticMethod("()Ljava/lang/Runtime$Version;")
    load = JavaMethod("(Ljava/lang/String;)V")
    loadLibrary = JavaMethod("(Ljava/lang/String;)V")
    gc = JavaMethod("()V")
    availableProcessors = JavaMethod("()I")
    freeMemory = JavaMethod("()J")
    maxMemory = JavaMethod("()J")
    exec = JavaMultipleMethod([("([Ljava/lang/String;)Ljava/lang/Process;", False, False), ("(Ljava/lang/String;[Ljava/lang/String;Ljava/io/File;)Ljava/lang/Process;", False, False), ("(Ljava/lang/String;)Ljava/lang/Process;", False, False), ("(Ljava/lang/String;[Ljava/lang/String;)Ljava/lang/Process;", False, False), ("([Ljava/lang/String;[Ljava/lang/String;)Ljava/lang/Process;", False, False), ("([Ljava/lang/String;[Ljava/lang/String;Ljava/io/File;)Ljava/lang/Process;", False, False)])
    halt = JavaMethod("(I)V")
    addShutdownHook = JavaMethod("(Ljava/lang/Thread;)V")
    removeShutdownHook = JavaMethod("(Ljava/lang/Thread;)Z")
    totalMemory = JavaMethod("()J")

    class Version(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "java/lang/Runtime$Version"
        equals = JavaMethod("(Ljava/lang/Object;)Z")
        toString = JavaMethod("()Ljava/lang/String;")
        version = JavaMethod("()Ljava/util/List;")
        hashCode = JavaMethod("()I")
        compareTo = JavaMultipleMethod([("(Ljava/lang/Runtime$Version;)I", False, False), ("(Ljava/lang/Object;)I", False, False)])
        update = JavaMethod("()I")
        feature = JavaMethod("()I")
        parse = JavaStaticMethod("(Ljava/lang/String;)Ljava/lang/Runtime$Version;")
        major = JavaMethod("()I")
        minor = JavaMethod("()I")
        pre = JavaMethod("()Ljava/util/Optional;")
        build = JavaMethod("()Ljava/util/Optional;")
        optional = JavaMethod("()Ljava/util/Optional;")
        interim = JavaMethod("()I")
        equalsIgnoreOptional = JavaMethod("(Ljava/lang/Object;)Z")
        patch = JavaMethod("()I")
        security = JavaMethod("()I")
        compareToIgnoreOptional = JavaMethod("(Ljava/lang/Runtime$Version;)I")