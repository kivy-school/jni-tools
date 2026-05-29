from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["BitmapFactory"]

class BitmapFactory(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/graphics/BitmapFactory"
    __javaconstructor__ = [("()V", False)]
    decodeFile = JavaMultipleMethod([("(Ljava/lang/String;Landroid/graphics/BitmapFactory$Options;)Landroid/graphics/Bitmap;", True, False), ("(Ljava/lang/String;)Landroid/graphics/Bitmap;", True, False)])
    decodeResourceStream = JavaStaticMethod("(Landroid/content/res/Resources;Landroid/util/TypedValue;Ljava/io/InputStream;Landroid/graphics/Rect;Landroid/graphics/BitmapFactory$Options;)Landroid/graphics/Bitmap;")
    decodeResource = JavaMultipleMethod([("(Landroid/content/res/Resources;ILandroid/graphics/BitmapFactory$Options;)Landroid/graphics/Bitmap;", True, False), ("(Landroid/content/res/Resources;I)Landroid/graphics/Bitmap;", True, False)])
    decodeByteArray = JavaMultipleMethod([("([BIILandroid/graphics/BitmapFactory$Options;)Landroid/graphics/Bitmap;", True, False), ("([BII)Landroid/graphics/Bitmap;", True, False)])
    decodeStream = JavaMultipleMethod([("(Ljava/io/InputStream;Landroid/graphics/Rect;Landroid/graphics/BitmapFactory$Options;)Landroid/graphics/Bitmap;", True, False), ("(Ljava/io/InputStream;)Landroid/graphics/Bitmap;", True, False)])
    decodeFileDescriptor = JavaMultipleMethod([("(Ljava/io/FileDescriptor;Landroid/graphics/Rect;Landroid/graphics/BitmapFactory$Options;)Landroid/graphics/Bitmap;", True, False), ("(Ljava/io/FileDescriptor;)Landroid/graphics/Bitmap;", True, False)])

    class Options(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/graphics/BitmapFactory/Options"
        __javaconstructor__ = [("()V", False)]
        inBitmap = JavaField("Landroid/graphics/Bitmap;")
        inDensity = JavaField("I")
        inDither = JavaField("Z")
        inInputShareable = JavaField("Z")
        inJustDecodeBounds = JavaField("Z")
        inMutable = JavaField("Z")
        inPreferQualityOverSpeed = JavaField("Z")
        inPreferredColorSpace = JavaField("Landroid/graphics/ColorSpace;")
        inPreferredConfig = JavaField("Landroid/graphics/Bitmap$Config;")
        inPremultiplied = JavaField("Z")
        inPurgeable = JavaField("Z")
        inSampleSize = JavaField("I")
        inScaled = JavaField("Z")
        inScreenDensity = JavaField("I")
        inTargetDensity = JavaField("I")
        inTempStorage = JavaField("[B")
        mCancel = JavaField("Z")
        outColorSpace = JavaField("Landroid/graphics/ColorSpace;")
        outConfig = JavaField("Landroid/graphics/Bitmap$Config;")
        outHeight = JavaField("I")
        outMimeType = JavaField("Ljava/lang/String;")
        outWidth = JavaField("I")
        requestCancelDecode = JavaMethod("()V")