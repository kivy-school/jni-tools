from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["InvalidPathException"]

class InvalidPathException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/file/InvalidPathException"
    __javaconstructor__ = [("(Ljava/lang/String;Ljava/lang/String;I)V", False), ("(Ljava/lang/String;Ljava/lang/String;)V", False)]
    getMessage = JavaMethod("()Ljava/lang/String;")
    getReason = JavaMethod("()Ljava/lang/String;")
    getInput = JavaMethod("()Ljava/lang/String;")
    getIndex = JavaMethod("()I")