from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SslErrorHandler"]

class SslErrorHandler(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/webkit/SslErrorHandler"
    cancel = JavaMethod("()V")
    proceed = JavaMethod("()V")