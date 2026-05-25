from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["DeniedByServerException"]

class DeniedByServerException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/media/DeniedByServerException"
    __javaconstructor__ = [("(Ljava/lang/String;)V", False)]