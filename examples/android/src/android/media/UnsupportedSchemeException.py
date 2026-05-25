from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["UnsupportedSchemeException"]

class UnsupportedSchemeException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/media/UnsupportedSchemeException"
    __javaconstructor__ = [("(Ljava/lang/String;)V", False)]