from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["LimitExceededException"]

class LimitExceededException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/os/LimitExceededException"
    __javaconstructor__ = [("()V", False), ("(Ljava/lang/String;)V", False)]