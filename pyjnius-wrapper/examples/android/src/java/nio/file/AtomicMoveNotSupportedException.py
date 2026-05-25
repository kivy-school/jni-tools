from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AtomicMoveNotSupportedException"]

class AtomicMoveNotSupportedException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/file/AtomicMoveNotSupportedException"
    __javaconstructor__ = [("(Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;)V", False)]