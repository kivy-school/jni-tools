from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["CleartextNetworkViolation"]

class CleartextNetworkViolation(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/os/strictmode/CleartextNetworkViolation"