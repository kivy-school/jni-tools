from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AnnotatedElement"]

class AnnotatedElement(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "java/lang/reflect/AnnotatedElement"
    isAnnotationPresent = JavaMethod("(Ljava/lang/Class;)Z")
    getAnnotation = JavaMethod("(Ljava/lang/Class;)Ljava/lang/annotation/Annotation;")
    getAnnotations = JavaMethod("()[Ljava/lang/annotation/Annotation;")
    getAnnotationsByType = JavaMethod("(Ljava/lang/Class;)[Ljava/lang/annotation/Annotation;")
    getDeclaredAnnotation = JavaMethod("(Ljava/lang/Class;)Ljava/lang/annotation/Annotation;")
    getDeclaredAnnotationsByType = JavaMethod("(Ljava/lang/Class;)[Ljava/lang/annotation/Annotation;")
    getDeclaredAnnotations = JavaMethod("()[Ljava/lang/annotation/Annotation;")