from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["IllegalFormatFlagsException"]

class IllegalFormatFlagsException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/IllegalFormatFlagsException"
    __javaconstructor__ = [("(Ljava/lang/String;)V", False)]
    getFlags = JavaMethod("()Ljava/lang/String;")
    getMessage = JavaMethod("()Ljava/lang/String;")