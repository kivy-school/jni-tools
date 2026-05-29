from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["StaleDataException"]

class StaleDataException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/database/StaleDataException"
    __javaconstructor__ = [("()V", False), ("(Ljava/lang/String;)V", False)]