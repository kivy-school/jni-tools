from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["MediaMetadataEditor"]

class MediaMetadataEditor(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/media/MediaMetadataEditor"
    BITMAP_KEY_ARTWORK = JavaStaticField("I")
    RATING_KEY_BY_OTHERS = JavaStaticField("I")
    RATING_KEY_BY_USER = JavaStaticField("I")
    getBitmap = JavaMethod("(ILandroid/graphics/Bitmap;)Landroid/graphics/Bitmap;")
    addEditableKey = JavaMethod("(I)V")
    getEditableKeys = JavaMethod("()[I")
    putBitmap = JavaMethod("(ILandroid/graphics/Bitmap;)Landroid/media/MediaMetadataEditor;")
    putObject = JavaMethod("(ILjava/lang/Object;)Landroid/media/MediaMetadataEditor;")
    removeEditableKeys = JavaMethod("()V")
    getObject = JavaMethod("(ILjava/lang/Object;)Ljava/lang/Object;")
    getLong = JavaMethod("(IJ)J")
    putLong = JavaMethod("(IJ)Landroid/media/MediaMetadataEditor;")
    clear = JavaMethod("()V")
    apply = JavaMethod("()V")
    getString = JavaMethod("(ILjava/lang/String;)Ljava/lang/String;")
    putString = JavaMethod("(ILjava/lang/String;)Landroid/media/MediaMetadataEditor;")