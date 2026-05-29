from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Throwable"]

class Throwable(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/lang/Throwable"
    __javaconstructor__ = [("(Ljava/lang/Throwable;)V", False), ("(Ljava/lang/String;Ljava/lang/Throwable;)V", False), ("(Ljava/lang/String;)V", False), ("()V", False)]
    printStackTrace = JavaMultipleMethod([("()V", False, False), ("(Ljava/io/PrintWriter;)V", False, False), ("(Ljava/io/PrintStream;)V", False, False)])
    getStackTrace = JavaMethod("()[Ljava/lang/StackTraceElement;")
    fillInStackTrace = JavaMethod("()Ljava/lang/Throwable;")
    getCause = JavaMethod("()Ljava/lang/Throwable;")
    initCause = JavaMethod("(Ljava/lang/Throwable;)Ljava/lang/Throwable;")
    toString = JavaMethod("()Ljava/lang/String;")
    addSuppressed = JavaMethod("(Ljava/lang/Throwable;)V")
    getMessage = JavaMethod("()Ljava/lang/String;")
    getSuppressed = JavaMethod("()[Ljava/lang/Throwable;")
    getLocalizedMessage = JavaMethod("()Ljava/lang/String;")
    setStackTrace = JavaMethod("([Ljava/lang/StackTraceElement;)V")