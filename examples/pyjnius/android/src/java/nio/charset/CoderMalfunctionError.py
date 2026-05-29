from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["CoderMalfunctionError"]

class CoderMalfunctionError(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/charset/CoderMalfunctionError"
    __javaconstructor__ = [("(Ljava/lang/Exception;)V", False)]