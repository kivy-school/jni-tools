from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["DatagramSocketImplFactory"]

class DatagramSocketImplFactory(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/net/DatagramSocketImplFactory"
    createDatagramSocketImpl = JavaMethod("()Ljava/net/DatagramSocketImpl;")