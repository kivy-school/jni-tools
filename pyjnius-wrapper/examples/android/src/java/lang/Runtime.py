from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Runtime"]

class Runtime(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/lang/Runtime"
    getRuntime = JavaStaticMethod("()Ljava/lang/Runtime;")
    exit = JavaMethod("(I)V")
    addShutdownHook = JavaMethod("(Ljava/lang/Thread;)V")
    removeShutdownHook = JavaMethod("(Ljava/lang/Thread;)Z")
    halt = JavaMethod("(I)V")
    runFinalizersOnExit = JavaStaticMethod("(Z)V")
    exec = JavaMultipleMethod([("(Ljava/lang/String;)Ljava/lang/Process;", False, False), ("(Ljava/lang/String;[Ljava/lang/String;)Ljava/lang/Process;", False, False), ("(Ljava/lang/String;[Ljava/lang/String;Ljava/io/File;)Ljava/lang/Process;", False, False), ("([Ljava/lang/String;)Ljava/lang/Process;", False, False), ("([Ljava/lang/String;[Ljava/lang/String;)Ljava/lang/Process;", False, False), ("([Ljava/lang/String;[Ljava/lang/String;Ljava/io/File;)Ljava/lang/Process;", False, False)])
    availableProcessors = JavaMethod("()I")
    freeMemory = JavaMethod("()J")
    totalMemory = JavaMethod("()J")
    maxMemory = JavaMethod("()J")
    gc = JavaMethod("()V")
    runFinalization = JavaMethod("()V")
    traceInstructions = JavaMethod("(Z)V")
    traceMethodCalls = JavaMethod("(Z)V")
    load = JavaMethod("(Ljava/lang/String;)V")
    loadLibrary = JavaMethod("(Ljava/lang/String;)V")