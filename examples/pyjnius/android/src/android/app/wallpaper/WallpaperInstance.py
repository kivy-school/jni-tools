from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["WallpaperInstance"]

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
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")