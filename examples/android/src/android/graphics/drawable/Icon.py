from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

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
    getType = JavaMethod("()I")
    getResPackage = JavaMethod("()Ljava/lang/String;")
    getResId = JavaMethod("()I")
    getUri = JavaMethod("()Landroid/net/Uri;")
    loadDrawableAsync = JavaMultipleMethod([("(Landroid/content/Context;Landroid/os/Message;)V", False, False), ("(Landroid/content/Context;Landroid/graphics/drawable/Icon$OnDrawableLoadedListener;Landroid/os/Handler;)V", False, False)])
    loadDrawable = JavaMethod("(Landroid/content/Context;)Landroid/graphics/drawable/Drawable;")
    createWithResource = JavaMultipleMethod([("(Landroid/content/Context;I)Landroid/graphics/drawable/Icon;", True, False), ("(Ljava/lang/String;I)Landroid/graphics/drawable/Icon;", True, False)])
    createWithBitmap = JavaStaticMethod("(Landroid/graphics/Bitmap;)Landroid/graphics/drawable/Icon;")
    createWithAdaptiveBitmap = JavaStaticMethod("(Landroid/graphics/Bitmap;)Landroid/graphics/drawable/Icon;")
    createWithData = JavaStaticMethod("([BII)Landroid/graphics/drawable/Icon;")
    createWithContentUri = JavaMultipleMethod([("(Ljava/lang/String;)Landroid/graphics/drawable/Icon;", True, False), ("(Landroid/net/Uri;)Landroid/graphics/drawable/Icon;", True, False)])
    createWithAdaptiveBitmapContentUri = JavaMultipleMethod([("(Ljava/lang/String;)Landroid/graphics/drawable/Icon;", True, False), ("(Landroid/net/Uri;)Landroid/graphics/drawable/Icon;", True, False)])
    setTint = JavaMethod("(I)Landroid/graphics/drawable/Icon;")
    setTintList = JavaMethod("(Landroid/content/res/ColorStateList;)Landroid/graphics/drawable/Icon;")
    setTintMode = JavaMethod("(Landroid/graphics/PorterDuff$Mode;)Landroid/graphics/drawable/Icon;")
    setTintBlendMode = JavaMethod("(Landroid/graphics/BlendMode;)Landroid/graphics/drawable/Icon;")
    createWithFilePath = JavaStaticMethod("(Ljava/lang/String;)Landroid/graphics/drawable/Icon;")
    toString = JavaMethod("()Ljava/lang/String;")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")

    class OnDrawableLoadedListener(JavaInterface, metaclass=MetaJavaClass):
        __javaclass__ = "android/graphics/drawable/Icon/OnDrawableLoadedListener"
        onDrawableLoaded = JavaMethod("(Landroid/graphics/drawable/Drawable;)V")