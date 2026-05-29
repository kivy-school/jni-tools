from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["DataOrigin"]

class DataOrigin(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/health/connect/datatypes/DataOrigin"
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    getPackageName = JavaMethod("()Ljava/lang/String;")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/health/connect/datatypes/DataOrigin$Builder"
        __javaconstructor__ = [("()V", False)]
        setPackageName = JavaMethod("(Ljava/lang/String;)Landroid/health/connect/datatypes/DataOrigin$Builder;")
        build = JavaMethod("()Landroid/health/connect/datatypes/DataOrigin;")