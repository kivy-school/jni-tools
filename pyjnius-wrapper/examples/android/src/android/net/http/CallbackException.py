from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["CallbackException"]

class CallbackException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/net/http/CallbackException"
    __javaconstructor__ = [("(Ljava/lang/String;Ljava/lang/Throwable;)V", False)]