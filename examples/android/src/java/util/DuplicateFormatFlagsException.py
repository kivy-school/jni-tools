from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["DuplicateFormatFlagsException"]

class DuplicateFormatFlagsException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/DuplicateFormatFlagsException"
    __javaconstructor__ = [("(Ljava/lang/String;)V", False)]
    getFlags = JavaMethod("()Ljava/lang/String;")
    getMessage = JavaMethod("()Ljava/lang/String;")