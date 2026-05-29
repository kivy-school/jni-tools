from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["WallpaperColors"]

class WallpaperColors(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/app/WallpaperColors"
    __javaconstructor__ = [("(Landroid/graphics/Color;Landroid/graphics/Color;Landroid/graphics/Color;)V", False), ("(Landroid/graphics/Color;Landroid/graphics/Color;Landroid/graphics/Color;I)V", False), ("(Landroid/os/Parcel;)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    HINT_SUPPORTS_DARK_TEXT = JavaStaticField("I")
    HINT_SUPPORTS_DARK_THEME = JavaStaticField("I")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    getColorHints = JavaMethod("()I")
    fromDrawable = JavaStaticMethod("(Landroid/graphics/drawable/Drawable;)Landroid/app/WallpaperColors;")
    getTertiaryColor = JavaMethod("()Landroid/graphics/Color;")
    getPrimaryColor = JavaMethod("()Landroid/graphics/Color;")
    getSecondaryColor = JavaMethod("()Landroid/graphics/Color;")
    fromBitmap = JavaStaticMethod("(Landroid/graphics/Bitmap;)Landroid/app/WallpaperColors;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")