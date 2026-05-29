from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SpellCheckerInfo"]

class SpellCheckerInfo(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/view/textservice/SpellCheckerInfo"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    getSubtypeAt = JavaMethod("(I)Landroid/view/textservice/SpellCheckerSubtype;")
    getSubtypeCount = JavaMethod("()I")
    getPackageName = JavaMethod("()Ljava/lang/String;")
    getId = JavaMethod("()Ljava/lang/String;")
    loadIcon = JavaMethod("(Landroid/content/pm/PackageManager;)Landroid/graphics/drawable/Drawable;")
    loadLabel = JavaMethod("(Landroid/content/pm/PackageManager;)Ljava/lang/CharSequence;")
    getServiceInfo = JavaMethod("()Landroid/content/pm/ServiceInfo;")
    getComponent = JavaMethod("()Landroid/content/ComponentName;")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")
    getSettingsActivity = JavaMethod("()Ljava/lang/String;")