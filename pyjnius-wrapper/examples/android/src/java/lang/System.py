from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["System"]

class System(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/lang/System"
    err = JavaStaticField("Ljava/io/PrintStream;")
    in = JavaStaticField("Ljava/io/InputStream;")
    out = JavaStaticField("Ljava/io/PrintStream;")
    setIn = JavaStaticMethod("(Ljava/io/InputStream;)V")
    setOut = JavaStaticMethod("(Ljava/io/PrintStream;)V")
    setErr = JavaStaticMethod("(Ljava/io/PrintStream;)V")
    console = JavaStaticMethod("()Ljava/io/Console;")
    inheritedChannel = JavaStaticMethod("()Ljava/nio/channels/Channel;")
    setSecurityManager = JavaStaticMethod("(Ljava/lang/SecurityManager;)V")
    getSecurityManager = JavaStaticMethod("()Ljava/lang/SecurityManager;")
    currentTimeMillis = JavaStaticMethod("()J")
    nanoTime = JavaStaticMethod("()J")
    arraycopy = JavaStaticMethod("(Ljava/lang/Object;ILjava/lang/Object;II)V")
    identityHashCode = JavaStaticMethod("(Ljava/lang/Object;)I")
    getProperties = JavaStaticMethod("()Ljava/util/Properties;")
    lineSeparator = JavaStaticMethod("()Ljava/lang/String;")
    setProperties = JavaStaticMethod("(Ljava/util/Properties;)V")
    getProperty = JavaMultipleMethod([("(Ljava/lang/String;)Ljava/lang/String;", True, False), ("(Ljava/lang/String;Ljava/lang/String;)Ljava/lang/String;", True, False)])
    setProperty = JavaStaticMethod("(Ljava/lang/String;Ljava/lang/String;)Ljava/lang/String;")
    clearProperty = JavaStaticMethod("(Ljava/lang/String;)Ljava/lang/String;")
    getenv = JavaMultipleMethod([("(Ljava/lang/String;)Ljava/lang/String;", True, False), ("()Ljava/util/Map;", True, False)])
    exit = JavaStaticMethod("(I)V")
    gc = JavaStaticMethod("()V")
    runFinalization = JavaStaticMethod("()V")
    runFinalizersOnExit = JavaStaticMethod("(Z)V")
    load = JavaStaticMethod("(Ljava/lang/String;)V")
    loadLibrary = JavaStaticMethod("(Ljava/lang/String;)V")
    mapLibraryName = JavaStaticMethod("(Ljava/lang/String;)Ljava/lang/String;")