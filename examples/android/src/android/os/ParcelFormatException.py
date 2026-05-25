from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ParcelFormatException"]

class ParcelFormatException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/os/ParcelFormatException"
    __javaconstructor__ = [("()V", False), ("(Ljava/lang/String;)V", False)]