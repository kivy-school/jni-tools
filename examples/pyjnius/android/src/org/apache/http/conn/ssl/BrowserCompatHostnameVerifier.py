from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["BrowserCompatHostnameVerifier"]

class BrowserCompatHostnameVerifier(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "org/apache/http/conn/ssl/BrowserCompatHostnameVerifier"
    __javaconstructor__ = [("()V", False)]
    toString = JavaMethod("()Ljava/lang/String;")
    verify = JavaMethod("(Ljava/lang/String;[Ljava/lang/String;[Ljava/lang/String;)V")