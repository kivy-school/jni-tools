from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["IncorrectContextUseViolation"]

class IncorrectContextUseViolation(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/os/strictmode/IncorrectContextUseViolation"
    __javaconstructor__ = [("(Ljava/lang/String;Ljava/lang/Throwable;)V", False)]