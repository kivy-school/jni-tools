from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["InetAddresses"]

class InetAddresses(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/net/InetAddresses"
    isNumericAddress = JavaStaticMethod("(Ljava/lang/String;)Z")
    parseNumericAddress = JavaStaticMethod("(Ljava/lang/String;)Ljava/net/InetAddress;")