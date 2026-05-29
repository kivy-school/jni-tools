from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AccessibleObject"]

class AccessibleObject(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/lang/reflect/AccessibleObject"
    __javaconstructor__ = [("()V", False)]
    setAccessible = JavaMultipleMethod([("([Ljava/lang/reflect/AccessibleObject;Z)V", True, False), ("(Z)V", False, False)])
    isAccessible = JavaMethod("()Z")
    getAnnotation = JavaMethod("(Ljava/lang/Class;)Ljava/lang/annotation/Annotation;")
    isAnnotationPresent = JavaMethod("(Ljava/lang/Class;)Z")
    getAnnotationsByType = JavaMethod("(Ljava/lang/Class;)[Ljava/lang/annotation/Annotation;")
    getAnnotations = JavaMethod("()[Ljava/lang/annotation/Annotation;")
    getDeclaredAnnotation = JavaMethod("(Ljava/lang/Class;)Ljava/lang/annotation/Annotation;")
    getDeclaredAnnotationsByType = JavaMethod("(Ljava/lang/Class;)[Ljava/lang/annotation/Annotation;")
    getDeclaredAnnotations = JavaMethod("()[Ljava/lang/annotation/Annotation;")