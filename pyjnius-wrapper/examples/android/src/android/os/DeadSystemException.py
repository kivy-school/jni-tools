from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["DeadSystemException"]

class DeadSystemException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/os/DeadSystemException"
    __javaconstructor__ = [("()V", False)]