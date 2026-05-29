from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["MissingFormatArgumentException"]

class MissingFormatArgumentException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/MissingFormatArgumentException"
    __javaconstructor__ = [("(Ljava/lang/String;)V", False)]
    getMessage = JavaMethod("()Ljava/lang/String;")
    getFormatSpecifier = JavaMethod("()Ljava/lang/String;")