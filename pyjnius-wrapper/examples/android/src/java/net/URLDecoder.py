from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["URLDecoder"]

class URLDecoder(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/net/URLDecoder"
    __javaconstructor__ = [("()V", False)]
    decode = JavaMultipleMethod([("(Ljava/lang/String;)Ljava/lang/String;", True, False), ("(Ljava/lang/String;Ljava/lang/String;)Ljava/lang/String;", True, False), ("(Ljava/lang/String;Ljava/nio/charset/Charset;)Ljava/lang/String;", True, False)])