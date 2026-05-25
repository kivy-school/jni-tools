from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["DatagramSocketImplFactory"]

class DatagramSocketImplFactory(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "java/net/DatagramSocketImplFactory"
    createDatagramSocketImpl = JavaMethod("()Ljava/net/DatagramSocketImpl;")