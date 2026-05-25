from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["MediaMetadataEditor"]

class MediaMetadataEditor(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/media/MediaMetadataEditor"
    BITMAP_KEY_ARTWORK = JavaStaticField("I")
    RATING_KEY_BY_OTHERS = JavaStaticField("I")
    RATING_KEY_BY_USER = JavaStaticField("I")
    apply = JavaMethod("()V")
    clear = JavaMethod("()V")
    addEditableKey = JavaMethod("(I)V")
    removeEditableKeys = JavaMethod("()V")
    getEditableKeys = JavaMethod("()[I")
    putString = JavaMethod("(ILjava/lang/String;)Landroid/media/MediaMetadataEditor;")
    putLong = JavaMethod("(IJ)Landroid/media/MediaMetadataEditor;")
    putBitmap = JavaMethod("(ILandroid/graphics/Bitmap;)Landroid/media/MediaMetadataEditor;")
    putObject = JavaMethod("(ILjava/lang/Object;)Landroid/media/MediaMetadataEditor;")
    getLong = JavaMethod("(IJ)J")
    getString = JavaMethod("(ILjava/lang/String;)Ljava/lang/String;")
    getBitmap = JavaMethod("(ILandroid/graphics/Bitmap;)Landroid/graphics/Bitmap;")
    getObject = JavaMethod("(ILjava/lang/Object;)Ljava/lang/Object;")