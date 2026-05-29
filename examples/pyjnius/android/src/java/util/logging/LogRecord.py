from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["LogRecord"]

class LogRecord(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/logging/LogRecord"
    __javaconstructor__ = [("(Ljava/util/logging/Level;Ljava/lang/String;)V", False)]
    setParameters = JavaMethod("([Ljava/lang/Object;)V")
    setMessage = JavaMethod("(Ljava/lang/String;)V")
    setSequenceNumber = JavaMethod("(J)V")
    getMessage = JavaMethod("()Ljava/lang/String;")
    getParameters = JavaMethod("()[Ljava/lang/Object;")
    getSequenceNumber = JavaMethod("()J")
    setMillis = JavaMethod("(J)V")
    getLoggerName = JavaMethod("()Ljava/lang/String;")
    getSourceClassName = JavaMethod("()Ljava/lang/String;")
    getSourceMethodName = JavaMethod("()Ljava/lang/String;")
    getThreadID = JavaMethod("()I")
    setThreadID = JavaMethod("(I)V")
    getLongThreadID = JavaMethod("()J")
    setLongThreadID = JavaMethod("(J)Ljava/util/logging/LogRecord;")
    getInstant = JavaMethod("()Ljava/time/Instant;")
    setInstant = JavaMethod("(Ljava/time/Instant;)V")
    getThrown = JavaMethod("()Ljava/lang/Throwable;")
    getLevel = JavaMethod("()Ljava/util/logging/Level;")
    setLevel = JavaMethod("(Ljava/util/logging/Level;)V")
    getMillis = JavaMethod("()J")
    getResourceBundleName = JavaMethod("()Ljava/lang/String;")
    setLoggerName = JavaMethod("(Ljava/lang/String;)V")
    setResourceBundleName = JavaMethod("(Ljava/lang/String;)V")
    setResourceBundle = JavaMethod("(Ljava/util/ResourceBundle;)V")
    setThrown = JavaMethod("(Ljava/lang/Throwable;)V")
    setSourceClassName = JavaMethod("(Ljava/lang/String;)V")
    setSourceMethodName = JavaMethod("(Ljava/lang/String;)V")
    getResourceBundle = JavaMethod("()Ljava/util/ResourceBundle;")