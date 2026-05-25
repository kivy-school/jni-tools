from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["FileUriExposedException"]

class FileUriExposedException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/os/FileUriExposedException"
    __javaconstructor__ = [("(Ljava/lang/String;)V", False)]