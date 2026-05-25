from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["PackageInfoHelper"]

class PackageInfoHelper(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/PackageInfoHelper"
    __javaconstructor__ = [("()V", False)]
    Companion = JavaStaticField("Lcom/onesignal/PackageInfoHelper$Companion;")

    class Companion(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "com/onesignal/PackageInfoHelper/Companion"
        getInfo = JavaMethod("(Landroid/content/Context;Ljava/lang/String;I)Lcom/onesignal/GetPackageInfoResult;")