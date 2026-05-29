from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Record"]

class Record(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/health/connect/datatypes/Record"
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    getMetadata = JavaMethod("()Landroid/health/connect/datatypes/Metadata;")