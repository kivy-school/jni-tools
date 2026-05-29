from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["WebResourceError"]

class WebResourceError(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/webkit/WebResourceError"
    getErrorCode = JavaMethod("()I")
    getDescription = JavaMethod("()Ljava/lang/CharSequence;")