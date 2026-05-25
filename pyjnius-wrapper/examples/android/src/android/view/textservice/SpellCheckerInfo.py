from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SpellCheckerInfo"]

class SpellCheckerInfo(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/view/textservice/SpellCheckerInfo"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    getId = JavaMethod("()Ljava/lang/String;")
    getComponent = JavaMethod("()Landroid/content/ComponentName;")
    getPackageName = JavaMethod("()Ljava/lang/String;")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    loadLabel = JavaMethod("(Landroid/content/pm/PackageManager;)Ljava/lang/CharSequence;")
    loadIcon = JavaMethod("(Landroid/content/pm/PackageManager;)Landroid/graphics/drawable/Drawable;")
    getServiceInfo = JavaMethod("()Landroid/content/pm/ServiceInfo;")
    getSettingsActivity = JavaMethod("()Ljava/lang/String;")
    getSubtypeCount = JavaMethod("()I")
    getSubtypeAt = JavaMethod("(I)Landroid/view/textservice/SpellCheckerSubtype;")
    describeContents = JavaMethod("()I")