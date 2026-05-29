from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["IllegalCharsetNameException"]

class IllegalCharsetNameException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/charset/IllegalCharsetNameException"
    __javaconstructor__ = [("(Ljava/lang/String;)V", False)]
    getCharsetName = JavaMethod("()Ljava/lang/String;")