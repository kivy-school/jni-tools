from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SocketImplFactory"]

class SocketImplFactory(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/net/SocketImplFactory"
    createSocketImpl = JavaMethod("()Ljava/net/SocketImpl;")