from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["GetPackageInfoResult"]

class GetPackageInfoResult(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/GetPackageInfoResult"
    __javaconstructor__ = [("(ZLandroid/content/pm/PackageInfo;)V", False)]
    getSuccessful = JavaMethod("()Z")
    getPackageInfo = JavaMethod("()Landroid/content/pm/PackageInfo;")
    component1 = JavaMethod("()Z")
    component2 = JavaMethod("()Landroid/content/pm/PackageInfo;")
    copy = JavaMethod("(ZLandroid/content/pm/PackageInfo;)Lcom/onesignal/GetPackageInfoResult;")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    equals = JavaMethod("(Ljava/lang/Object;)Z")