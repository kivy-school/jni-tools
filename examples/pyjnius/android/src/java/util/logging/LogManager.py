from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["LogManager"]

class LogManager(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/logging/LogManager"
    LOGGING_MXBEAN_NAME = JavaStaticField("Ljava/lang/String;")
    reset = JavaMethod("()V")
    getProperty = JavaMethod("(Ljava/lang/String;)Ljava/lang/String;")
    getLogger = JavaMethod("(Ljava/lang/String;)Ljava/util/logging/Logger;")
    checkAccess = JavaMethod("()V")
    updateConfiguration = JavaMultipleMethod([("(Ljava/util/function/Function;)V", False, False), ("(Ljava/io/InputStream;Ljava/util/function/Function;)V", False, False)])
    addLogger = JavaMethod("(Ljava/util/logging/Logger;)Z")
    readConfiguration = JavaMultipleMethod([("()V", False, False), ("(Ljava/io/InputStream;)V", False, False)])
    getLoggerNames = JavaMethod("()Ljava/util/Enumeration;")
    getLoggingMXBean = JavaStaticMethod("()Ljava/util/logging/LoggingMXBean;")
    addConfigurationListener = JavaMethod("(Ljava/lang/Runnable;)Ljava/util/logging/LogManager;")
    removeConfigurationListener = JavaMethod("(Ljava/lang/Runnable;)V")
    getLogManager = JavaStaticMethod("()Ljava/util/logging/LogManager;")