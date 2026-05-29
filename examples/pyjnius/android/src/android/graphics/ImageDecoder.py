from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ImageDecoder"]

class ImageDecoder(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/graphics/ImageDecoder"
    ALLOCATOR_DEFAULT = JavaStaticField("I")
    ALLOCATOR_HARDWARE = JavaStaticField("I")
    ALLOCATOR_SHARED_MEMORY = JavaStaticField("I")
    ALLOCATOR_SOFTWARE = JavaStaticField("I")
    MEMORY_POLICY_DEFAULT = JavaStaticField("I")
    MEMORY_POLICY_LOW_RAM = JavaStaticField("I")
    setTargetSize = JavaMethod("(II)V")
    isMutableRequired = JavaMethod("()Z")
    decodeBitmap = JavaMultipleMethod([("(Landroid/graphics/ImageDecoder$Source;Landroid/graphics/ImageDecoder$OnHeaderDecodedListener;)Landroid/graphics/Bitmap;", True, False), ("(Landroid/graphics/ImageDecoder$Source;)Landroid/graphics/Bitmap;", True, False)])
    getPostProcessor = JavaMethod("()Landroid/graphics/PostProcessor;")
    setMutableRequired = JavaMethod("(Z)V")
    getAllocator = JavaMethod("()I")
    getCrop = JavaMethod("()Landroid/graphics/Rect;")
    setAllocator = JavaMethod("(I)V")
    setPostProcessor = JavaMethod("(Landroid/graphics/PostProcessor;)V")
    createSource = JavaMultipleMethod([("([B)Landroid/graphics/ImageDecoder$Source;", True, False), ("(Landroid/content/ContentResolver;Landroid/net/Uri;)Landroid/graphics/ImageDecoder$Source;", True, False), ("(Ljava/util/concurrent/Callable;)Landroid/graphics/ImageDecoder$Source;", True, False), ("(Ljava/nio/ByteBuffer;)Landroid/graphics/ImageDecoder$Source;", True, False), ("(Ljava/io/File;)Landroid/graphics/ImageDecoder$Source;", True, False), ("([BII)Landroid/graphics/ImageDecoder$Source;", True, False), ("(Landroid/content/res/AssetManager;Ljava/lang/String;)Landroid/graphics/ImageDecoder$Source;", True, False), ("(Landroid/content/res/Resources;I)Landroid/graphics/ImageDecoder$Source;", True, False)])
    decodeDrawable = JavaMultipleMethod([("(Landroid/graphics/ImageDecoder$Source;Landroid/graphics/ImageDecoder$OnHeaderDecodedListener;)Landroid/graphics/drawable/Drawable;", True, False), ("(Landroid/graphics/ImageDecoder$Source;)Landroid/graphics/drawable/Drawable;", True, False)])
    getMemorySizePolicy = JavaMethod("()I")
    getOnPartialImageListener = JavaMethod("()Landroid/graphics/ImageDecoder$OnPartialImageListener;")
    isDecodeAsAlphaMaskEnabled = JavaMethod("()Z")
    isMimeTypeSupported = JavaStaticMethod("(Ljava/lang/String;)Z")
    isUnpremultipliedRequired = JavaMethod("()Z")
    setDecodeAsAlphaMaskEnabled = JavaMethod("(Z)V")
    setMemorySizePolicy = JavaMethod("(I)V")
    setOnPartialImageListener = JavaMethod("(Landroid/graphics/ImageDecoder$OnPartialImageListener;)V")
    setTargetColorSpace = JavaMethod("(Landroid/graphics/ColorSpace;)V")
    setTargetSampleSize = JavaMethod("(I)V")
    setUnpremultipliedRequired = JavaMethod("(Z)V")
    close = JavaMethod("()V")
    setCrop = JavaMethod("(Landroid/graphics/Rect;)V")

    class Source(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/graphics/ImageDecoder$Source"

    class OnPartialImageListener(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/graphics/ImageDecoder$OnPartialImageListener"
        onPartialImage = JavaMethod("(Landroid/graphics/ImageDecoder$DecodeException;)Z")

    class OnHeaderDecodedListener(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/graphics/ImageDecoder$OnHeaderDecodedListener"
        onHeaderDecoded = JavaMethod("(Landroid/graphics/ImageDecoder;Landroid/graphics/ImageDecoder$ImageInfo;Landroid/graphics/ImageDecoder$Source;)V")

    class ImageInfo(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/graphics/ImageDecoder$ImageInfo"
        isAnimated = JavaMethod("()Z")
        getSize = JavaMethod("()Landroid/util/Size;")
        getColorSpace = JavaMethod("()Landroid/graphics/ColorSpace;")
        getMimeType = JavaMethod("()Ljava/lang/String;")

    class DecodeException(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/graphics/ImageDecoder$DecodeException"
        SOURCE_EXCEPTION = JavaStaticField("I")
        SOURCE_INCOMPLETE = JavaStaticField("I")
        SOURCE_MALFORMED_DATA = JavaStaticField("I")
        getError = JavaMethod("()I")
        getSource = JavaMethod("()Landroid/graphics/ImageDecoder$Source;")