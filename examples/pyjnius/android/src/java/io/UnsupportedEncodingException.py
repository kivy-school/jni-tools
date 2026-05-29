from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["UnsupportedEncodingException"]

class UnsupportedEncodingException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/io/UnsupportedEncodingException"
    __javaconstructor__ = [("()V", False), ("(Ljava/lang/String;)V", False)]