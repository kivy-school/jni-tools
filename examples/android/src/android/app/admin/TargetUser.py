from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["TargetUser"]

class TargetUser(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/app/admin/TargetUser"
    GLOBAL = JavaStaticField("Landroid/app/admin/TargetUser;")
    LOCAL_USER = JavaStaticField("Landroid/app/admin/TargetUser;")
    PARENT_USER = JavaStaticField("Landroid/app/admin/TargetUser;")
    UNKNOWN_USER = JavaStaticField("Landroid/app/admin/TargetUser;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")