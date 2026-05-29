from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["WallpaperInfo"]

class WallpaperInfo(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/app/WallpaperInfo"
    __javaconstructor__ = [("(Landroid/content/Context;Landroid/content/pm/ResolveInfo;)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    getPackageName = JavaMethod("()Ljava/lang/String;")
    getServiceName = JavaMethod("()Ljava/lang/String;")
    getServiceInfo = JavaMethod("()Landroid/content/pm/ServiceInfo;")
    getComponent = JavaMethod("()Landroid/content/ComponentName;")
    loadLabel = JavaMethod("(Landroid/content/pm/PackageManager;)Ljava/lang/CharSequence;")
    loadIcon = JavaMethod("(Landroid/content/pm/PackageManager;)Landroid/graphics/drawable/Drawable;")
    loadThumbnail = JavaMethod("(Landroid/content/pm/PackageManager;)Landroid/graphics/drawable/Drawable;")
    loadAuthor = JavaMethod("(Landroid/content/pm/PackageManager;)Ljava/lang/CharSequence;")
    loadDescription = JavaMethod("(Landroid/content/pm/PackageManager;)Ljava/lang/CharSequence;")
    loadContextUri = JavaMethod("(Landroid/content/pm/PackageManager;)Landroid/net/Uri;")
    loadContextDescription = JavaMethod("(Landroid/content/pm/PackageManager;)Ljava/lang/CharSequence;")
    getShowMetadataInPreview = JavaMethod("()Z")
    getSettingsActivity = JavaMethod("()Ljava/lang/String;")
    getSettingsSliceUri = JavaMethod("()Landroid/net/Uri;")
    supportsMultipleDisplays = JavaMethod("()Z")
    shouldUseDefaultUnfoldTransition = JavaMethod("()Z")
    dump = JavaMethod("(Landroid/util/Printer;Ljava/lang/String;)V")
    toString = JavaMethod("()Ljava/lang/String;")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")