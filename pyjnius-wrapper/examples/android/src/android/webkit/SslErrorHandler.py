from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SslErrorHandler"]

class SslErrorHandler(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/webkit/SslErrorHandler"
    proceed = JavaMethod("()V")
    cancel = JavaMethod("()V")