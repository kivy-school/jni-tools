from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["StackWalker"]

class StackWalker(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/lang/StackWalker"
    getInstance = JavaMultipleMethod([("()Ljava/lang/StackWalker;", True, False), ("(Ljava/lang/StackWalker$Option;)Ljava/lang/StackWalker;", True, False), ("(Ljava/util/Set;)Ljava/lang/StackWalker;", True, False), ("(Ljava/util/Set;I)Ljava/lang/StackWalker;", True, False)])
    walk = JavaMethod("(Ljava/util/function/Function;)Ljava/lang/Object;")
    forEach = JavaMethod("(Ljava/util/function/Consumer;)V")
    getCallerClass = JavaMethod("()Ljava/lang/Class;")

    class Option(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "java/lang/StackWalker/Option"
        values = JavaStaticMethod("()[Ljava/lang/StackWalker$Option;")
        valueOf = JavaStaticMethod("(Ljava/lang/String;)Ljava/lang/StackWalker$Option;")
        RETAIN_CLASS_REFERENCE = JavaStaticField("Ljava/lang/StackWalker/Option;")
        SHOW_REFLECT_FRAMES = JavaStaticField("Ljava/lang/StackWalker/Option;")
        SHOW_HIDDEN_FRAMES = JavaStaticField("Ljava/lang/StackWalker/Option;")

    class StackFrame(JavaInterface, metaclass=MetaJavaClass):
        __javaclass__ = "java/lang/StackWalker/StackFrame"
        getClassName = JavaMethod("()Ljava/lang/String;")
        getMethodName = JavaMethod("()Ljava/lang/String;")
        getDeclaringClass = JavaMethod("()Ljava/lang/Class;")
        getMethodType = JavaMethod("()Ljava/lang/invoke/MethodType;")
        getDescriptor = JavaMethod("()Ljava/lang/String;")
        getByteCodeIndex = JavaMethod("()I")
        getFileName = JavaMethod("()Ljava/lang/String;")
        getLineNumber = JavaMethod("()I")
        isNativeMethod = JavaMethod("()Z")
        toStackTraceElement = JavaMethod("()Ljava/lang/StackTraceElement;")