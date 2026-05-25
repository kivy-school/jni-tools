from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SocketImplFactory"]

class SocketImplFactory(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "java/net/SocketImplFactory"
    createSocketImpl = JavaMethod("()Ljava/net/SocketImpl;")