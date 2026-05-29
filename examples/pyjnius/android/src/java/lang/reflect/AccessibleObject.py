from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AccessibleObject"]

class AccessibleObject(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/lang/reflect/AccessibleObject"
    setAccessible = JavaMultipleMethod([("([Ljava/lang/reflect/AccessibleObject;Z)V", True, False), ("(Z)V", False, False)])
    isAnnotationPresent = JavaMethod("(Ljava/lang/Class;)Z")
    getAnnotation = JavaMethod("(Ljava/lang/Class;)Ljava/lang/annotation/Annotation;")
    getAnnotationsByType = JavaMethod("(Ljava/lang/Class;)[Ljava/lang/annotation/Annotation;")
    getAnnotations = JavaMethod("()[Ljava/lang/annotation/Annotation;")
    getDeclaredAnnotation = JavaMethod("(Ljava/lang/Class;)Ljava/lang/annotation/Annotation;")
    getDeclaredAnnotationsByType = JavaMethod("(Ljava/lang/Class;)[Ljava/lang/annotation/Annotation;")
    getDeclaredAnnotations = JavaMethod("()[Ljava/lang/annotation/Annotation;")
    trySetAccessible = JavaMethod("()Z")
    canAccess = JavaMethod("(Ljava/lang/Object;)Z")
    isAccessible = JavaMethod("()Z")