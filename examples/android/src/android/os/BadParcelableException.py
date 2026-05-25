from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["BadParcelableException"]

class BadParcelableException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/os/BadParcelableException"
    __javaconstructor__ = [("(Ljava/lang/String;)V", False), ("(Ljava/lang/Exception;)V", False)]