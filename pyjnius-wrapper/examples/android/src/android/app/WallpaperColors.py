from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["WallpaperColors"]

class WallpaperColors(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/app/WallpaperColors"
    __javaconstructor__ = [("(Landroid/os/Parcel;)V", False), ("(Landroid/graphics/Color;Landroid/graphics/Color;Landroid/graphics/Color;)V", False), ("(Landroid/graphics/Color;Landroid/graphics/Color;Landroid/graphics/Color;I)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    HINT_SUPPORTS_DARK_TEXT = JavaStaticField("I")
    HINT_SUPPORTS_DARK_THEME = JavaStaticField("I")
    fromDrawable = JavaStaticMethod("(Landroid/graphics/drawable/Drawable;)Landroid/app/WallpaperColors;")
    fromBitmap = JavaStaticMethod("(Landroid/graphics/Bitmap;)Landroid/app/WallpaperColors;")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    getPrimaryColor = JavaMethod("()Landroid/graphics/Color;")
    getSecondaryColor = JavaMethod("()Landroid/graphics/Color;")
    getTertiaryColor = JavaMethod("()Landroid/graphics/Color;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    getColorHints = JavaMethod("()I")
    toString = JavaMethod("()Ljava/lang/String;")