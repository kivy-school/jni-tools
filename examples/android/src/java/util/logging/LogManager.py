from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["LogManager"]

class LogManager(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/logging/LogManager"
    __javaconstructor__ = [("()V", False)]
    LOGGING_MXBEAN_NAME = JavaStaticField("Ljava/lang/String;")
    getLogManager = JavaStaticMethod("()Ljava/util/logging/LogManager;")
    addPropertyChangeListener = JavaMethod("(Ljava/beans/PropertyChangeListener;)V")
    removePropertyChangeListener = JavaMethod("(Ljava/beans/PropertyChangeListener;)V")
    addLogger = JavaMethod("(Ljava/util/logging/Logger;)Z")
    getLogger = JavaMethod("(Ljava/lang/String;)Ljava/util/logging/Logger;")
    getLoggerNames = JavaMethod("()Ljava/util/Enumeration;")
    readConfiguration = JavaMultipleMethod([("()V", False, False), ("(Ljava/io/InputStream;)V", False, False)])
    reset = JavaMethod("()V")
    getProperty = JavaMethod("(Ljava/lang/String;)Ljava/lang/String;")
    checkAccess = JavaMethod("()V")
    getLoggingMXBean = JavaStaticMethod("()Ljava/util/logging/LoggingMXBean;")