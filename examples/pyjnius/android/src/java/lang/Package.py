from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Package"]

class Package(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/lang/Package"
    getName = JavaMethod("()Ljava/lang/String;")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    isSealed = JavaMultipleMethod([("(Ljava/net/URL;)Z", False, False), ("()Z", False, False)])
    isAnnotationPresent = JavaMethod("(Ljava/lang/Class;)Z")
    getPackage = JavaStaticMethod("(Ljava/lang/String;)Ljava/lang/Package;")
    getAnnotation = JavaMethod("(Ljava/lang/Class;)Ljava/lang/annotation/Annotation;")
    getAnnotationsByType = JavaMethod("(Ljava/lang/Class;)[Ljava/lang/annotation/Annotation;")
    getAnnotations = JavaMethod("()[Ljava/lang/annotation/Annotation;")
    getDeclaredAnnotation = JavaMethod("(Ljava/lang/Class;)Ljava/lang/annotation/Annotation;")
    getDeclaredAnnotationsByType = JavaMethod("(Ljava/lang/Class;)[Ljava/lang/annotation/Annotation;")
    getDeclaredAnnotations = JavaMethod("()[Ljava/lang/annotation/Annotation;")
    getPackages = JavaStaticMethod("()[Ljava/lang/Package;")
    getSpecificationTitle = JavaMethod("()Ljava/lang/String;")
    getSpecificationVersion = JavaMethod("()Ljava/lang/String;")
    getSpecificationVendor = JavaMethod("()Ljava/lang/String;")
    getImplementationTitle = JavaMethod("()Ljava/lang/String;")
    getImplementationVersion = JavaMethod("()Ljava/lang/String;")
    getImplementationVendor = JavaMethod("()Ljava/lang/String;")
    isCompatibleWith = JavaMethod("(Ljava/lang/String;)Z")