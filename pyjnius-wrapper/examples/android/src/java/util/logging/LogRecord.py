from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["LogRecord"]

class LogRecord(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/logging/LogRecord"
    __javaconstructor__ = [("(Ljava/util/logging/Level;Ljava/lang/String;)V", False)]
    getLoggerName = JavaMethod("()Ljava/lang/String;")
    setLoggerName = JavaMethod("(Ljava/lang/String;)V")
    getResourceBundle = JavaMethod("()Ljava/util/ResourceBundle;")
    setResourceBundle = JavaMethod("(Ljava/util/ResourceBundle;)V")
    getResourceBundleName = JavaMethod("()Ljava/lang/String;")
    setResourceBundleName = JavaMethod("(Ljava/lang/String;)V")
    getLevel = JavaMethod("()Ljava/util/logging/Level;")
    setLevel = JavaMethod("(Ljava/util/logging/Level;)V")
    getSequenceNumber = JavaMethod("()J")
    setSequenceNumber = JavaMethod("(J)V")
    getSourceClassName = JavaMethod("()Ljava/lang/String;")
    setSourceClassName = JavaMethod("(Ljava/lang/String;)V")
    getSourceMethodName = JavaMethod("()Ljava/lang/String;")
    setSourceMethodName = JavaMethod("(Ljava/lang/String;)V")
    getMessage = JavaMethod("()Ljava/lang/String;")
    setMessage = JavaMethod("(Ljava/lang/String;)V")
    getParameters = JavaMethod("()[Ljava/lang/Object;")
    setParameters = JavaMethod("([Ljava/lang/Object;)V")
    getThreadID = JavaMethod("()I")
    setThreadID = JavaMethod("(I)V")
    getMillis = JavaMethod("()J")
    setMillis = JavaMethod("(J)V")
    getThrown = JavaMethod("()Ljava/lang/Throwable;")
    setThrown = JavaMethod("(Ljava/lang/Throwable;)V")