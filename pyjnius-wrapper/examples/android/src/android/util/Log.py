from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Log"]

class Log(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/util/Log"
    ASSERT = JavaStaticField("I")
    DEBUG = JavaStaticField("I")
    ERROR = JavaStaticField("I")
    INFO = JavaStaticField("I")
    VERBOSE = JavaStaticField("I")
    WARN = JavaStaticField("I")
    v = JavaMultipleMethod([("(Ljava/lang/String;Ljava/lang/String;)I", True, False), ("(Ljava/lang/String;Ljava/lang/String;Ljava/lang/Throwable;)I", True, False)])
    d = JavaMultipleMethod([("(Ljava/lang/String;Ljava/lang/String;)I", True, False), ("(Ljava/lang/String;Ljava/lang/String;Ljava/lang/Throwable;)I", True, False)])
    i = JavaMultipleMethod([("(Ljava/lang/String;Ljava/lang/String;)I", True, False), ("(Ljava/lang/String;Ljava/lang/String;Ljava/lang/Throwable;)I", True, False)])
    w = JavaMultipleMethod([("(Ljava/lang/String;Ljava/lang/String;)I", True, False), ("(Ljava/lang/String;Ljava/lang/String;Ljava/lang/Throwable;)I", True, False), ("(Ljava/lang/String;Ljava/lang/Throwable;)I", True, False)])
    isLoggable = JavaStaticMethod("(Ljava/lang/String;I)Z")
    e = JavaMultipleMethod([("(Ljava/lang/String;Ljava/lang/String;)I", True, False), ("(Ljava/lang/String;Ljava/lang/String;Ljava/lang/Throwable;)I", True, False)])
    wtf = JavaMultipleMethod([("(Ljava/lang/String;Ljava/lang/String;)I", True, False), ("(Ljava/lang/String;Ljava/lang/Throwable;)I", True, False), ("(Ljava/lang/String;Ljava/lang/String;Ljava/lang/Throwable;)I", True, False)])
    getStackTraceString = JavaStaticMethod("(Ljava/lang/Throwable;)Ljava/lang/String;")
    println = JavaStaticMethod("(ILjava/lang/String;Ljava/lang/String;)I")