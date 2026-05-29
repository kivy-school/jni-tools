from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["OSLogger"]

class OSLogger(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/OSLogger"
    verbose = JavaMethod("(Ljava/lang/String;)V")
    debug = JavaMethod("(Ljava/lang/String;)V")
    info = JavaMethod("(Ljava/lang/String;)V")
    warning = JavaMethod("(Ljava/lang/String;)V")
    error = JavaMultipleMethod([("(Ljava/lang/String;)V", False, False), ("(Ljava/lang/String;Ljava/lang/Throwable;)V", False, False)])