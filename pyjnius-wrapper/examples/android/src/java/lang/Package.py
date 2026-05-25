from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Package"]

class Package(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/lang/Package"
    getName = JavaMethod("()Ljava/lang/String;")
    getSpecificationTitle = JavaMethod("()Ljava/lang/String;")
    getSpecificationVersion = JavaMethod("()Ljava/lang/String;")
    getSpecificationVendor = JavaMethod("()Ljava/lang/String;")
    getImplementationTitle = JavaMethod("()Ljava/lang/String;")
    getImplementationVersion = JavaMethod("()Ljava/lang/String;")
    getImplementationVendor = JavaMethod("()Ljava/lang/String;")
    isSealed = JavaMultipleMethod([("()Z", False, False), ("(Ljava/net/URL;)Z", False, False)])
    isCompatibleWith = JavaMethod("(Ljava/lang/String;)Z")
    getPackage = JavaStaticMethod("(Ljava/lang/String;)Ljava/lang/Package;")
    getPackages = JavaStaticMethod("()[Ljava/lang/Package;")
    hashCode = JavaMethod("()I")
    toString = JavaMethod("()Ljava/lang/String;")
    getAnnotation = JavaMethod("(Ljava/lang/Class;)Ljava/lang/annotation/Annotation;")
    isAnnotationPresent = JavaMethod("(Ljava/lang/Class;)Z")
    getAnnotationsByType = JavaMethod("(Ljava/lang/Class;)[Ljava/lang/annotation/Annotation;")
    getAnnotations = JavaMethod("()[Ljava/lang/annotation/Annotation;")
    getDeclaredAnnotation = JavaMethod("(Ljava/lang/Class;)Ljava/lang/annotation/Annotation;")
    getDeclaredAnnotationsByType = JavaMethod("(Ljava/lang/Class;)[Ljava/lang/annotation/Annotation;")
    getDeclaredAnnotations = JavaMethod("()[Ljava/lang/annotation/Annotation;")