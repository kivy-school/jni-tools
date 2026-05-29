from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["DeadObjectException"]

class DeadObjectException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/os/DeadObjectException"
    __javaconstructor__ = [("()V", False), ("(Ljava/lang/String;)V", False)]