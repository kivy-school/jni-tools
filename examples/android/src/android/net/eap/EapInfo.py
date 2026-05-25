from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["EapInfo"]

class EapInfo(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/net/eap/EapInfo"
    getEapMethodType = JavaMethod("()I")