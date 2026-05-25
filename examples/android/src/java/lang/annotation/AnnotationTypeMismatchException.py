from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AnnotationTypeMismatchException"]

class AnnotationTypeMismatchException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/lang/annotation/AnnotationTypeMismatchException"
    __javaconstructor__ = [("(Ljava/lang/reflect/Method;Ljava/lang/String;)V", False)]
    element = JavaMethod("()Ljava/lang/reflect/Method;")
    foundType = JavaMethod("()Ljava/lang/String;")