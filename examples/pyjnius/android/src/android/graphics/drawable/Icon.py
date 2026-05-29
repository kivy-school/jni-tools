from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Icon"]

class Icon(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/graphics/drawable/Icon"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    TYPE_ADAPTIVE_BITMAP = JavaStaticField("I")
    TYPE_BITMAP = JavaStaticField("I")
    TYPE_DATA = JavaStaticField("I")
    TYPE_RESOURCE = JavaStaticField("I")
    TYPE_URI = JavaStaticField("I")
    TYPE_URI_ADAPTIVE_BITMAP = JavaStaticField("I")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    toString = JavaMethod("()Ljava/lang/String;")
    getType = JavaMethod("()I")
    createWithAdaptiveBitmap = JavaStaticMethod("(Landroid/graphics/Bitmap;)Landroid/graphics/drawable/Icon;")
    createWithAdaptiveBitmapContentUri = JavaMultipleMethod([("(Landroid/net/Uri;)Landroid/graphics/drawable/Icon;", True, False), ("(Ljava/lang/String;)Landroid/graphics/drawable/Icon;", True, False)])
    createWithBitmap = JavaStaticMethod("(Landroid/graphics/Bitmap;)Landroid/graphics/drawable/Icon;")
    createWithContentUri = JavaMultipleMethod([("(Ljava/lang/String;)Landroid/graphics/drawable/Icon;", True, False), ("(Landroid/net/Uri;)Landroid/graphics/drawable/Icon;", True, False)])
    createWithData = JavaStaticMethod("([BII)Landroid/graphics/drawable/Icon;")
    createWithFilePath = JavaStaticMethod("(Ljava/lang/String;)Landroid/graphics/drawable/Icon;")
    createWithResource = JavaMultipleMethod([("(Ljava/lang/String;I)Landroid/graphics/drawable/Icon;", True, False), ("(Landroid/content/Context;I)Landroid/graphics/drawable/Icon;", True, False)])
    getResId = JavaMethod("()I")
    getResPackage = JavaMethod("()Ljava/lang/String;")
    getUri = JavaMethod("()Landroid/net/Uri;")
    loadDrawable = JavaMethod("(Landroid/content/Context;)Landroid/graphics/drawable/Drawable;")
    loadDrawableAsync = JavaMultipleMethod([("(Landroid/content/Context;Landroid/graphics/drawable/Icon$OnDrawableLoadedListener;Landroid/os/Handler;)V", False, False), ("(Landroid/content/Context;Landroid/os/Message;)V", False, False)])
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")
    setTint = JavaMethod("(I)Landroid/graphics/drawable/Icon;")
    setTintBlendMode = JavaMethod("(Landroid/graphics/BlendMode;)Landroid/graphics/drawable/Icon;")
    setTintList = JavaMethod("(Landroid/content/res/ColorStateList;)Landroid/graphics/drawable/Icon;")
    setTintMode = JavaMethod("(Landroid/graphics/PorterDuff$Mode;)Landroid/graphics/drawable/Icon;")

    class OnDrawableLoadedListener(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/graphics/drawable/Icon$OnDrawableLoadedListener"
        onDrawableLoaded = JavaMethod("(Landroid/graphics/drawable/Drawable;)V")