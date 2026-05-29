from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["PackageIdentifier"]

class PackageIdentifier(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/app/appsearch/PackageIdentifier"
    __javaconstructor__ = [("(Ljava/lang/String;[B)V", False)]
    getSha256Certificate = JavaMethod("()[B")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    getPackageName = JavaMethod("()Ljava/lang/String;")