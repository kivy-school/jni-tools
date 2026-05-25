from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["InvalidPathException"]

class InvalidPathException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/file/InvalidPathException"
    __javaconstructor__ = [("(Ljava/lang/String;Ljava/lang/String;I)V", False), ("(Ljava/lang/String;Ljava/lang/String;)V", False)]
    getInput = JavaMethod("()Ljava/lang/String;")
    getReason = JavaMethod("()Ljava/lang/String;")
    getIndex = JavaMethod("()I")
    getMessage = JavaMethod("()Ljava/lang/String;")