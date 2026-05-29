from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["NetworkOnMainThreadException"]

class NetworkOnMainThreadException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/os/NetworkOnMainThreadException"
    __javaconstructor__ = [("()V", False)]