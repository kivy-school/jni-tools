from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SocketOption"]

class SocketOption(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/net/SocketOption"
    name = JavaMethod("()Ljava/lang/String;")
    type = JavaMethod("()Ljava/lang/Class;")