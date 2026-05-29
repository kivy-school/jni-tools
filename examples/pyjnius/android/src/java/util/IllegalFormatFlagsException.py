from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["IllegalFormatFlagsException"]

class IllegalFormatFlagsException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/IllegalFormatFlagsException"
    __javaconstructor__ = [("(Ljava/lang/String;)V", False)]
    getMessage = JavaMethod("()Ljava/lang/String;")
    getFlags = JavaMethod("()Ljava/lang/String;")