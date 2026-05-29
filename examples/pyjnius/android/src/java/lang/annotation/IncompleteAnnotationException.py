from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["IncompleteAnnotationException"]

class IncompleteAnnotationException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/lang/annotation/IncompleteAnnotationException"
    __javaconstructor__ = [("(Ljava/lang/Class;Ljava/lang/String;)V", False)]
    annotationType = JavaMethod("()Ljava/lang/Class;")
    elementName = JavaMethod("()Ljava/lang/String;")