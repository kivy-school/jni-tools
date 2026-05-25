from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["QuicException"]

class QuicException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/net/http/QuicException"
    __javaconstructor__ = [("(Ljava/lang/String;Ljava/lang/Throwable;)V", False)]