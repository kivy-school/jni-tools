from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ComponentInfo"]

class ComponentInfo(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/content/pm/ComponentInfo"
    __javaconstructor__ = [("()V", False), ("(Landroid/content/pm/ComponentInfo;)V", False), ("(Landroid/os/Parcel;)V", False)]
    applicationInfo = JavaField("Landroid/content/pm/ApplicationInfo;")
    attributionTags = JavaField("[Ljava/lang/String;")
    descriptionRes = JavaField("I")
    directBootAware = JavaField("Z")
    enabled = JavaField("Z")
    exported = JavaField("Z")
    processName = JavaField("Ljava/lang/String;")
    splitName = JavaField("Ljava/lang/String;")
    isEnabled = JavaMethod("()Z")
    getIconResource = JavaMethod("()I")
    getLogoResource = JavaMethod("()I")
    getBannerResource = JavaMethod("()I")
    dumpFront = JavaMethod("(Landroid/util/Printer;Ljava/lang/String;)V")
    dumpBack = JavaMethod("(Landroid/util/Printer;Ljava/lang/String;)V")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")