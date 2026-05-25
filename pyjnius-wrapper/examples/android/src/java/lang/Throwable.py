from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Throwable"]

class Throwable(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/lang/Throwable"
    __javaconstructor__ = [("()V", False), ("(Ljava/lang/String;)V", False), ("(Ljava/lang/String;Ljava/lang/Throwable;)V", False), ("(Ljava/lang/Throwable;)V", False), ("(Ljava/lang/String;Ljava/lang/Throwable;ZZ)V", False)]
    getMessage = JavaMethod("()Ljava/lang/String;")
    getLocalizedMessage = JavaMethod("()Ljava/lang/String;")
    getCause = JavaMethod("()Ljava/lang/Throwable;")
    initCause = JavaMethod("(Ljava/lang/Throwable;)Ljava/lang/Throwable;")
    toString = JavaMethod("()Ljava/lang/String;")
    printStackTrace = JavaMultipleMethod([("()V", False, False), ("(Ljava/io/PrintStream;)V", False, False), ("(Ljava/io/PrintWriter;)V", False, False)])
    fillInStackTrace = JavaMethod("()Ljava/lang/Throwable;")
    getStackTrace = JavaMethod("()[Ljava/lang/StackTraceElement;")
    setStackTrace = JavaMethod("([Ljava/lang/StackTraceElement;)V")
    addSuppressed = JavaMethod("(Ljava/lang/Throwable;)V")
    getSuppressed = JavaMethod("()[Ljava/lang/Throwable;")