from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["TransportInfo"]

class TransportInfo(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/net/TransportInfo"