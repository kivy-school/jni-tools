from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["WallpaperInfo"]

class WallpaperInfo(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/app/WallpaperInfo"
    __javaconstructor__ = [("(Landroid/content/Context;Landroid/content/pm/ResolveInfo;)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    loadContextUri = JavaMethod("(Landroid/content/pm/PackageManager;)Landroid/net/Uri;")
    loadAuthor = JavaMethod("(Landroid/content/pm/PackageManager;)Ljava/lang/CharSequence;")
    getSettingsSliceUri = JavaMethod("()Landroid/net/Uri;")
    getShowMetadataInPreview = JavaMethod("()Z")
    loadContextDescription = JavaMethod("(Landroid/content/pm/PackageManager;)Ljava/lang/CharSequence;")
    shouldUseDefaultUnfoldTransition = JavaMethod("()Z")
    supportsMultipleDisplays = JavaMethod("()Z")
    toString = JavaMethod("()Ljava/lang/String;")
    getPackageName = JavaMethod("()Ljava/lang/String;")
    dump = JavaMethod("(Landroid/util/Printer;Ljava/lang/String;)V")
    loadIcon = JavaMethod("(Landroid/content/pm/PackageManager;)Landroid/graphics/drawable/Drawable;")
    loadLabel = JavaMethod("(Landroid/content/pm/PackageManager;)Ljava/lang/CharSequence;")
    loadThumbnail = JavaMethod("(Landroid/content/pm/PackageManager;)Landroid/graphics/drawable/Drawable;")
    loadDescription = JavaMethod("(Landroid/content/pm/PackageManager;)Ljava/lang/CharSequence;")
    getServiceInfo = JavaMethod("()Landroid/content/pm/ServiceInfo;")
    getComponent = JavaMethod("()Landroid/content/ComponentName;")
    getServiceName = JavaMethod("()Ljava/lang/String;")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")
    getSettingsActivity = JavaMethod("()Ljava/lang/String;")