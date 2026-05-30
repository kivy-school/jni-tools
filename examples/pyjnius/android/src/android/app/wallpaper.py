from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

class WallpaperInstance(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/app/wallpaper/WallpaperInstance"
    __javaconstructor__ = [("(Landroid/app/WallpaperInfo;Landroid/app/wallpaper/WallpaperDescription;)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    getInfo = JavaMethod("()Landroid/app/WallpaperInfo;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    getId = JavaMethod("()Ljava/lang/String;")
    getDescription = JavaMethod("()Landroid/app/wallpaper/WallpaperDescription;")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")

class WallpaperDescription(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/app/wallpaper/WallpaperDescription"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    toBuilder = JavaMethod("()Landroid/app/wallpaper/WallpaperDescription$Builder;")
    getThumbnail = JavaMethod("()Landroid/net/Uri;")
    getContextDescription = JavaMethod("()Ljava/lang/CharSequence;")
    getContextUri = JavaMethod("()Landroid/net/Uri;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    getId = JavaMethod("()Ljava/lang/String;")
    getDescription = JavaMethod("()Ljava/util/List;")
    getComponent = JavaMethod("()Landroid/content/ComponentName;")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    getTitle = JavaMethod("()Ljava/lang/CharSequence;")
    getContent = JavaMethod("()Landroid/os/PersistableBundle;")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/app/wallpaper/WallpaperDescription$Builder"
        __javaconstructor__ = [("()V", False)]
        setContextDescription = JavaMethod("(Ljava/lang/CharSequence;)Landroid/app/wallpaper/WallpaperDescription$Builder;")
        setContextUri = JavaMethod("(Landroid/net/Uri;)Landroid/app/wallpaper/WallpaperDescription$Builder;")
        setDescription = JavaMethod("(Ljava/util/List;)Landroid/app/wallpaper/WallpaperDescription$Builder;")
        setId = JavaMethod("(Ljava/lang/String;)Landroid/app/wallpaper/WallpaperDescription$Builder;")
        setThumbnail = JavaMethod("(Landroid/net/Uri;)Landroid/app/wallpaper/WallpaperDescription$Builder;")
        setContent = JavaMethod("(Landroid/os/PersistableBundle;)Landroid/app/wallpaper/WallpaperDescription$Builder;")
        build = JavaMethod("()Landroid/app/wallpaper/WallpaperDescription;")
        setTitle = JavaMethod("(Ljava/lang/CharSequence;)Landroid/app/wallpaper/WallpaperDescription$Builder;")