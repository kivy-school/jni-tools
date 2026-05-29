from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["LoggingMXBean"]

class LoggingMXBean(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/logging/LoggingMXBean"
    getLoggerNames = JavaMethod("()Ljava/util/List;")
    getLoggerLevel = JavaMethod("(Ljava/lang/String;)Ljava/lang/String;")
    setLoggerLevel = JavaMethod("(Ljava/lang/String;Ljava/lang/String;)V")
    getParentLoggerName = JavaMethod("(Ljava/lang/String;)Ljava/lang/String;")