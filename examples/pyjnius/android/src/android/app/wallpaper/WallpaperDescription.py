from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["WallpaperDescription"]

class WallpaperDescription(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/app/wallpaper/WallpaperDescription"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    toBuilder = JavaMethod("()Landroid/app/wallpaper/WallpaperDescription$Builder;")
    getContextUri = JavaMethod("()Landroid/net/Uri;")
    getContextDescription = JavaMethod("()Ljava/lang/CharSequence;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    getId = JavaMethod("()Ljava/lang/String;")
    getContent = JavaMethod("()Landroid/os/PersistableBundle;")
    getTitle = JavaMethod("()Ljava/lang/CharSequence;")
    getComponent = JavaMethod("()Landroid/content/ComponentName;")
    getDescription = JavaMethod("()Ljava/util/List;")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")
    getThumbnail = JavaMethod("()Landroid/net/Uri;")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/app/wallpaper/WallpaperDescription$Builder"
        __javaconstructor__ = [("()V", False)]
        setContextUri = JavaMethod("(Landroid/net/Uri;)Landroid/app/wallpaper/WallpaperDescription$Builder;")
        setContextDescription = JavaMethod("(Ljava/lang/CharSequence;)Landroid/app/wallpaper/WallpaperDescription$Builder;")
        setContent = JavaMethod("(Landroid/os/PersistableBundle;)Landroid/app/wallpaper/WallpaperDescription$Builder;")
        setId = JavaMethod("(Ljava/lang/String;)Landroid/app/wallpaper/WallpaperDescription$Builder;")
        setTitle = JavaMethod("(Ljava/lang/CharSequence;)Landroid/app/wallpaper/WallpaperDescription$Builder;")
        setDescription = JavaMethod("(Ljava/util/List;)Landroid/app/wallpaper/WallpaperDescription$Builder;")
        build = JavaMethod("()Landroid/app/wallpaper/WallpaperDescription;")
        setThumbnail = JavaMethod("(Landroid/net/Uri;)Landroid/app/wallpaper/WallpaperDescription$Builder;")