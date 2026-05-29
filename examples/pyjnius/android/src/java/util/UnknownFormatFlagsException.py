from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["UnknownFormatFlagsException"]

class UnknownFormatFlagsException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/UnknownFormatFlagsException"
    __javaconstructor__ = [("(Ljava/lang/String;)V", False)]
    getMessage = JavaMethod("()Ljava/lang/String;")
    getFlags = JavaMethod("()Ljava/lang/String;")