from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["FileLockInterruptionException"]

class FileLockInterruptionException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/channels/FileLockInterruptionException"
    __javaconstructor__ = [("()V", False)]