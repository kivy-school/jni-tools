from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["System"]

class System(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/lang/System"
    in = JavaStaticField("Ljava/io/InputStream;")
    out = JavaStaticField("Ljava/io/PrintStream;")
    err = JavaStaticField("Ljava/io/PrintStream;")
    exit = JavaStaticMethod("(I)V")
    runFinalization = JavaStaticMethod("()V")
    getProperty = JavaMultipleMethod([("(Ljava/lang/String;)Ljava/lang/String;", True, False), ("(Ljava/lang/String;Ljava/lang/String;)Ljava/lang/String;", True, False)])
    identityHashCode = JavaStaticMethod("(Ljava/lang/Object;)I")
    currentTimeMillis = JavaStaticMethod("()J")
    nanoTime = JavaStaticMethod("()J")
    arraycopy = JavaStaticMethod("(Ljava/lang/Object;ILjava/lang/Object;II)V")
    load = JavaStaticMethod("(Ljava/lang/String;)V")
    loadLibrary = JavaStaticMethod("(Ljava/lang/String;)V")
    console = JavaStaticMethod("()Ljava/io/Console;")
    inheritedChannel = JavaStaticMethod("()Ljava/nio/channels/Channel;")
    lineSeparator = JavaStaticMethod("()Ljava/lang/String;")
    setProperty = JavaStaticMethod("(Ljava/lang/String;Ljava/lang/String;)Ljava/lang/String;")
    getenv = JavaMultipleMethod([("(Ljava/lang/String;)Ljava/lang/String;", True, False), ("()Ljava/util/Map;", True, False)])
    getLogger = JavaMultipleMethod([("(Ljava/lang/String;)Ljava/lang/System$Logger;", True, False), ("(Ljava/lang/String;Ljava/util/ResourceBundle;)Ljava/lang/System$Logger;", True, False)])
    gc = JavaStaticMethod("()V")
    setIn = JavaStaticMethod("(Ljava/io/InputStream;)V")
    setOut = JavaStaticMethod("(Ljava/io/PrintStream;)V")
    setErr = JavaStaticMethod("(Ljava/io/PrintStream;)V")
    setSecurityManager = JavaStaticMethod("(Ljava/lang/SecurityManager;)V")
    getSecurityManager = JavaStaticMethod("()Ljava/lang/SecurityManager;")
    getProperties = JavaStaticMethod("()Ljava/util/Properties;")
    setProperties = JavaStaticMethod("(Ljava/util/Properties;)V")
    clearProperty = JavaStaticMethod("(Ljava/lang/String;)Ljava/lang/String;")
    mapLibraryName = JavaStaticMethod("(Ljava/lang/String;)Ljava/lang/String;")

    class Logger(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "java/lang/System$Logger"
        isLoggable = JavaMethod("(Ljava/lang/System$Logger$Level;)Z")
        getName = JavaMethod("()Ljava/lang/String;")
        log = JavaMultipleMethod([("(Ljava/lang/System$Logger$Level;Ljava/lang/String;[Ljava/lang/Object;)V", False, True), ("(Ljava/lang/System$Logger$Level;Ljava/util/function/Supplier;Ljava/lang/Throwable;)V", False, False), ("(Ljava/lang/System$Logger$Level;Ljava/util/ResourceBundle;Ljava/lang/String;Ljava/lang/Throwable;)V", False, False), ("(Ljava/lang/System$Logger$Level;Ljava/util/ResourceBundle;Ljava/lang/String;[Ljava/lang/Object;)V", False, True), ("(Ljava/lang/System$Logger$Level;Ljava/lang/String;)V", False, False), ("(Ljava/lang/System$Logger$Level;Ljava/util/function/Supplier;)V", False, False), ("(Ljava/lang/System$Logger$Level;Ljava/lang/Object;)V", False, False), ("(Ljava/lang/System$Logger$Level;Ljava/lang/String;Ljava/lang/Throwable;)V", False, False)])

        class Level(JavaClass, metaclass=MetaJavaClass):
            __javaclass__ = "java/lang/System$Logger$Level"
            ALL = JavaStaticField("Ljava/lang/System$Logger$Level;")
            TRACE = JavaStaticField("Ljava/lang/System$Logger$Level;")
            DEBUG = JavaStaticField("Ljava/lang/System$Logger$Level;")
            INFO = JavaStaticField("Ljava/lang/System$Logger$Level;")
            WARNING = JavaStaticField("Ljava/lang/System$Logger$Level;")
            ERROR = JavaStaticField("Ljava/lang/System$Logger$Level;")
            OFF = JavaStaticField("Ljava/lang/System$Logger$Level;")
            getName = JavaMethod("()Ljava/lang/String;")
            values = JavaStaticMethod("()[Ljava/lang/System$Logger$Level;")
            valueOf = JavaStaticMethod("(Ljava/lang/String;)Ljava/lang/System$Logger$Level;")
            getSeverity = JavaMethod("()I")
            ALL = JavaStaticField("Ljava/lang/System$Logger$Level;")
            TRACE = JavaStaticField("Ljava/lang/System$Logger$Level;")
            DEBUG = JavaStaticField("Ljava/lang/System$Logger$Level;")
            INFO = JavaStaticField("Ljava/lang/System$Logger$Level;")
            WARNING = JavaStaticField("Ljava/lang/System$Logger$Level;")
            ERROR = JavaStaticField("Ljava/lang/System$Logger$Level;")
            OFF = JavaStaticField("Ljava/lang/System$Logger$Level;")

    class LoggerFinder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "java/lang/System$LoggerFinder"
        getLogger = JavaMethod("(Ljava/lang/String;Ljava/lang/Module;)Ljava/lang/System$Logger;")
        getLocalizedLogger = JavaMethod("(Ljava/lang/String;Ljava/util/ResourceBundle;Ljava/lang/Module;)Ljava/lang/System$Logger;")
        getLoggerFinder = JavaStaticMethod("()Ljava/lang/System$LoggerFinder;")