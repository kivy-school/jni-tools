from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["NetworkSpecifier"]

class NetworkSpecifier(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/net/NetworkSpecifier"
    __javaconstructor__ = [("()V", False)]