from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AnnotationFormatError"]

class AnnotationFormatError(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/lang/annotation/AnnotationFormatError"
    __javaconstructor__ = [("(Ljava/lang/String;)V", False), ("(Ljava/lang/String;Ljava/lang/Throwable;)V", False), ("(Ljava/lang/Throwable;)V", False)]