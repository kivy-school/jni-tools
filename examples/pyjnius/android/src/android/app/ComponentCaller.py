from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ComponentCaller"]

class ComponentCaller(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/app/ComponentCaller"
    getUid = JavaMethod("()I")
    getPackage = JavaMethod("()Ljava/lang/String;")
    checkContentUriPermission = JavaMethod("(Landroid/net/Uri;I)I")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")