from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["PeerHandle"]

class PeerHandle(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/net/wifi/aware/PeerHandle"
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")