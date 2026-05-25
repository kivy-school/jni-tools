from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["BrowserCompatHostnameVerifier"]

class BrowserCompatHostnameVerifier(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "org/apache/http/conn/ssl/BrowserCompatHostnameVerifier"
    __javaconstructor__ = [("()V", False)]
    verify = JavaMethod("(Ljava/lang/String;[Ljava/lang/String;[Ljava/lang/String;)V")
    toString = JavaMethod("()Ljava/lang/String;")