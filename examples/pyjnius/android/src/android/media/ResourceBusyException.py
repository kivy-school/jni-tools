from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ResourceBusyException"]

class ResourceBusyException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/media/ResourceBusyException"
    __javaconstructor__ = [("(Ljava/lang/String;)V", False)]