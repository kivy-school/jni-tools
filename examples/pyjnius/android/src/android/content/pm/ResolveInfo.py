from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ResolveInfo"]

class ResolveInfo(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/content/pm/ResolveInfo"
    __javaconstructor__ = [("()V", False), ("(Landroid/content/pm/ResolveInfo;)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    activityInfo = JavaField("Landroid/content/pm/ActivityInfo;")
    filter = JavaField("Landroid/content/IntentFilter;")
    icon = JavaField("I")
    isDefault = JavaField("Z")
    isInstantAppAvailable = JavaField("Z")
    labelRes = JavaField("I")
    match = JavaField("I")
    nonLocalizedLabel = JavaField("Ljava/lang/CharSequence;")
    preferredOrder = JavaField("I")
    priority = JavaField("I")
    providerInfo = JavaField("Landroid/content/pm/ProviderInfo;")
    resolvePackageName = JavaField("Ljava/lang/String;")
    serviceInfo = JavaField("Landroid/content/pm/ServiceInfo;")
    specificIndex = JavaField("I")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    toString = JavaMethod("()Ljava/lang/String;")
    dump = JavaMethod("(Landroid/util/Printer;Ljava/lang/String;)V")
    getIconResource = JavaMethod("()I")
    loadIcon = JavaMethod("(Landroid/content/pm/PackageManager;)Landroid/graphics/drawable/Drawable;")
    loadLabel = JavaMethod("(Landroid/content/pm/PackageManager;)Ljava/lang/CharSequence;")
    isCrossProfileIntentForwarderActivity = JavaMethod("()Z")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")

    class DisplayNameComparator(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/content/pm/ResolveInfo$DisplayNameComparator"
        __javaconstructor__ = [("(Landroid/content/pm/PackageManager;)V", False)]
        compare = JavaMultipleMethod([("(Landroid/content/pm/ResolveInfo;Landroid/content/pm/ResolveInfo;)I", False, False), ("(Ljava/lang/Object;Ljava/lang/Object;)I", False, False)])