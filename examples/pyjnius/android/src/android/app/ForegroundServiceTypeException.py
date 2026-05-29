from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ForegroundServiceTypeException"]

class ForegroundServiceTypeException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/app/ForegroundServiceTypeException"
    __javaconstructor__ = [("(Ljava/lang/String;)V", False)]