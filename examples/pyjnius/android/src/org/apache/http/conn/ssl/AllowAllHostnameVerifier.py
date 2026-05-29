from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AllowAllHostnameVerifier"]

class AllowAllHostnameVerifier(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "org/apache/http/conn/ssl/AllowAllHostnameVerifier"
    __javaconstructor__ = [("()V", False)]
    toString = JavaMethod("()Ljava/lang/String;")
    verify = JavaMethod("(Ljava/lang/String;[Ljava/lang/String;[Ljava/lang/String;)V")