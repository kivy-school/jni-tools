from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["TransportInfo"]

class TransportInfo(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "android/net/TransportInfo"