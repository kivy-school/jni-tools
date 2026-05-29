from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["PackageItemInfo"]

class PackageItemInfo(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/content/pm/PackageItemInfo"
    __javaconstructor__ = [("()V", False), ("(Landroid/content/pm/PackageItemInfo;)V", False), ("(Landroid/os/Parcel;)V", False)]
    banner = JavaField("I")
    icon = JavaField("I")
    isArchived = JavaField("Z")
    labelRes = JavaField("I")
    logo = JavaField("I")
    metaData = JavaField("Landroid/os/Bundle;")
    name = JavaField("Ljava/lang/String;")
    nonLocalizedLabel = JavaField("Ljava/lang/CharSequence;")
    packageName = JavaField("Ljava/lang/String;")
    loadLabel = JavaMethod("(Landroid/content/pm/PackageManager;)Ljava/lang/CharSequence;")
    loadIcon = JavaMethod("(Landroid/content/pm/PackageManager;)Landroid/graphics/drawable/Drawable;")
    loadUnbadgedIcon = JavaMethod("(Landroid/content/pm/PackageManager;)Landroid/graphics/drawable/Drawable;")
    loadBanner = JavaMethod("(Landroid/content/pm/PackageManager;)Landroid/graphics/drawable/Drawable;")
    loadLogo = JavaMethod("(Landroid/content/pm/PackageManager;)Landroid/graphics/drawable/Drawable;")
    loadXmlMetaData = JavaMethod("(Landroid/content/pm/PackageManager;Ljava/lang/String;)Landroid/content/res/XmlResourceParser;")
    dumpFront = JavaMethod("(Landroid/util/Printer;Ljava/lang/String;)V")
    dumpBack = JavaMethod("(Landroid/util/Printer;Ljava/lang/String;)V")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")

    class DisplayNameComparator(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/content/pm/PackageItemInfo/DisplayNameComparator"
        __javaconstructor__ = [("(Landroid/content/pm/PackageManager;)V", False)]
        compare = JavaMethod("(Landroid/content/pm/PackageItemInfo;Landroid/content/pm/PackageItemInfo;)I")