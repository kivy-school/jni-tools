from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["UnsupportedCharsetException"]

class UnsupportedCharsetException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/charset/UnsupportedCharsetException"
    __javaconstructor__ = [("(Ljava/lang/String;)V", False)]
    getCharsetName = JavaMethod("()Ljava/lang/String;")