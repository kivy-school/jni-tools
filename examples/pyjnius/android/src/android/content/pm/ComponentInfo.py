from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ComponentInfo"]

class ComponentInfo(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/content/pm/ComponentInfo"
    __javaconstructor__ = [("(Landroid/content/pm/ComponentInfo;)V", False), ("()V", False)]
    applicationInfo = JavaField("Landroid/content/pm/ApplicationInfo;")
    attributionTags = JavaField("[Ljava/lang/String;")
    descriptionRes = JavaField("I")
    directBootAware = JavaField("Z")
    enabled = JavaField("Z")
    exported = JavaField("Z")
    processName = JavaField("Ljava/lang/String;")
    splitName = JavaField("Ljava/lang/String;")
    banner = JavaField("I")
    icon = JavaField("I")
    isArchived = JavaField("Z")
    labelRes = JavaField("I")
    logo = JavaField("I")
    metaData = JavaField("Landroid/os/Bundle;")
    name = JavaField("Ljava/lang/String;")
    nonLocalizedLabel = JavaField("Ljava/lang/CharSequence;")
    packageName = JavaField("Ljava/lang/String;")
    isEnabled = JavaMethod("()Z")
    getBannerResource = JavaMethod("()I")
    getIconResource = JavaMethod("()I")
    getLogoResource = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")