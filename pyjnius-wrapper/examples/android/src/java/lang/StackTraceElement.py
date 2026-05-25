from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["StackTraceElement"]

class StackTraceElement(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/lang/StackTraceElement"
    __javaconstructor__ = [("(Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;I)V", False)]
    getFileName = JavaMethod("()Ljava/lang/String;")
    getLineNumber = JavaMethod("()I")
    getClassName = JavaMethod("()Ljava/lang/String;")
    getMethodName = JavaMethod("()Ljava/lang/String;")
    isNativeMethod = JavaMethod("()Z")
    toString = JavaMethod("()Ljava/lang/String;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")