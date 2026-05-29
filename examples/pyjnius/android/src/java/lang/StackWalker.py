from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["StackWalker"]

class StackWalker(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/lang/StackWalker"
    getCallerClass = JavaMethod("()Ljava/lang/Class;")
    getInstance = JavaMultipleMethod([("(Ljava/lang/StackWalker$Option;)Ljava/lang/StackWalker;", True, False), ("(Ljava/util/Set;)Ljava/lang/StackWalker;", True, False), ("(Ljava/util/Set;I)Ljava/lang/StackWalker;", True, False), ("()Ljava/lang/StackWalker;", True, False)])
    forEach = JavaMethod("(Ljava/util/function/Consumer;)V")
    walk = JavaMethod("(Ljava/util/function/Function;)Ljava/lang/Object;")

    class Option(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "java/lang/StackWalker$Option"
        RETAIN_CLASS_REFERENCE = JavaStaticField("Ljava/lang/StackWalker$Option;")
        DROP_METHOD_INFO = JavaStaticField("Ljava/lang/StackWalker$Option;")
        SHOW_REFLECT_FRAMES = JavaStaticField("Ljava/lang/StackWalker$Option;")
        SHOW_HIDDEN_FRAMES = JavaStaticField("Ljava/lang/StackWalker$Option;")
        values = JavaStaticMethod("()[Ljava/lang/StackWalker$Option;")
        valueOf = JavaStaticMethod("(Ljava/lang/String;)Ljava/lang/StackWalker$Option;")
        RETAIN_CLASS_REFERENCE = JavaStaticField("Ljava/lang/StackWalker$Option;")
        DROP_METHOD_INFO = JavaStaticField("Ljava/lang/StackWalker$Option;")
        SHOW_REFLECT_FRAMES = JavaStaticField("Ljava/lang/StackWalker$Option;")
        SHOW_HIDDEN_FRAMES = JavaStaticField("Ljava/lang/StackWalker$Option;")

    class StackFrame(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "java/lang/StackWalker$StackFrame"
        getDescriptor = JavaMethod("()Ljava/lang/String;")
        getDeclaringClass = JavaMethod("()Ljava/lang/Class;")
        toStackTraceElement = JavaMethod("()Ljava/lang/StackTraceElement;")
        getMethodType = JavaMethod("()Ljava/lang/invoke/MethodType;")
        getClassName = JavaMethod("()Ljava/lang/String;")
        getByteCodeIndex = JavaMethod("()I")
        isNativeMethod = JavaMethod("()Z")
        getFileName = JavaMethod("()Ljava/lang/String;")
        getLineNumber = JavaMethod("()I")
        getMethodName = JavaMethod("()Ljava/lang/String;")