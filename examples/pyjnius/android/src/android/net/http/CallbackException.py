from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["CallbackException"]

class CallbackException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/net/http/CallbackException"