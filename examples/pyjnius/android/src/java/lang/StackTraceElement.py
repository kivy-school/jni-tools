from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["StackTraceElement"]

class StackTraceElement(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/lang/StackTraceElement"
    __javaconstructor__ = [("(Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;I)V", False), ("(Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;I)V", False)]
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    getClassName = JavaMethod("()Ljava/lang/String;")
    isNativeMethod = JavaMethod("()Z")
    getFileName = JavaMethod("()Ljava/lang/String;")
    getLineNumber = JavaMethod("()I")
    getModuleName = JavaMethod("()Ljava/lang/String;")
    getModuleVersion = JavaMethod("()Ljava/lang/String;")
    getClassLoaderName = JavaMethod("()Ljava/lang/String;")
    getMethodName = JavaMethod("()Ljava/lang/String;")