from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SocketOption"]

class SocketOption(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "java/net/SocketOption"
    name = JavaMethod("()Ljava/lang/String;")
    type = JavaMethod("()Ljava/lang/Class;")