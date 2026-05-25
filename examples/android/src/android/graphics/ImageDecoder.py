from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ImageDecoder"]

class ImageDecoder(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/graphics/ImageDecoder"
    ALLOCATOR_DEFAULT = JavaStaticField("I")
    ALLOCATOR_HARDWARE = JavaStaticField("I")
    ALLOCATOR_SHARED_MEMORY = JavaStaticField("I")
    ALLOCATOR_SOFTWARE = JavaStaticField("I")
    MEMORY_POLICY_DEFAULT = JavaStaticField("I")
    MEMORY_POLICY_LOW_RAM = JavaStaticField("I")
    finalize = JavaMethod("()V")
    isMimeTypeSupported = JavaStaticMethod("(Ljava/lang/String;)Z")
    createSource = JavaMultipleMethod([("(Landroid/content/res/Resources;I)Landroid/graphics/ImageDecoder$Source;", True, False), ("(Landroid/content/ContentResolver;Landroid/net/Uri;)Landroid/graphics/ImageDecoder$Source;", True, False), ("(Landroid/content/res/AssetManager;Ljava/lang/String;)Landroid/graphics/ImageDecoder$Source;", True, False), ("([BII)Landroid/graphics/ImageDecoder$Source;", True, False), ("([B)Landroid/graphics/ImageDecoder$Source;", True, False), ("(Ljava/nio/ByteBuffer;)Landroid/graphics/ImageDecoder$Source;", True, False), ("(Ljava/io/File;)Landroid/graphics/ImageDecoder$Source;", True, False), ("(Ljava/util/concurrent/Callable;)Landroid/graphics/ImageDecoder$Source;", True, False)])
    setTargetSize = JavaMethod("(II)V")
    setTargetSampleSize = JavaMethod("(I)V")
    setAllocator = JavaMethod("(I)V")
    getAllocator = JavaMethod("()I")
    setUnpremultipliedRequired = JavaMethod("(Z)V")
    isUnpremultipliedRequired = JavaMethod("()Z")
    setPostProcessor = JavaMethod("(Landroid/graphics/PostProcessor;)V")
    getPostProcessor = JavaMethod("()Landroid/graphics/PostProcessor;")
    setOnPartialImageListener = JavaMethod("(Landroid/graphics/ImageDecoder$OnPartialImageListener;)V")
    getOnPartialImageListener = JavaMethod("()Landroid/graphics/ImageDecoder$OnPartialImageListener;")
    setCrop = JavaMethod("(Landroid/graphics/Rect;)V")
    getCrop = JavaMethod("()Landroid/graphics/Rect;")
    setMutableRequired = JavaMethod("(Z)V")
    isMutableRequired = JavaMethod("()Z")
    setMemorySizePolicy = JavaMethod("(I)V")
    getMemorySizePolicy = JavaMethod("()I")
    setDecodeAsAlphaMaskEnabled = JavaMethod("(Z)V")
    isDecodeAsAlphaMaskEnabled = JavaMethod("()Z")
    setTargetColorSpace = JavaMethod("(Landroid/graphics/ColorSpace;)V")
    close = JavaMethod("()V")
    decodeDrawable = JavaMultipleMethod([("(Landroid/graphics/ImageDecoder$Source;Landroid/graphics/ImageDecoder$OnHeaderDecodedListener;)Landroid/graphics/drawable/Drawable;", True, False), ("(Landroid/graphics/ImageDecoder$Source;)Landroid/graphics/drawable/Drawable;", True, False)])
    decodeBitmap = JavaMultipleMethod([("(Landroid/graphics/ImageDecoder$Source;Landroid/graphics/ImageDecoder$OnHeaderDecodedListener;)Landroid/graphics/Bitmap;", True, False), ("(Landroid/graphics/ImageDecoder$Source;)Landroid/graphics/Bitmap;", True, False)])

    class DecodeException(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/graphics/ImageDecoder/DecodeException"
        SOURCE_EXCEPTION = JavaStaticField("I")
        SOURCE_INCOMPLETE = JavaStaticField("I")
        SOURCE_MALFORMED_DATA = JavaStaticField("I")
        getError = JavaMethod("()I")
        getSource = JavaMethod("()Landroid/graphics/ImageDecoder$Source;")

    class ImageInfo(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/graphics/ImageDecoder/ImageInfo"
        getSize = JavaMethod("()Landroid/util/Size;")
        getMimeType = JavaMethod("()Ljava/lang/String;")
        isAnimated = JavaMethod("()Z")
        getColorSpace = JavaMethod("()Landroid/graphics/ColorSpace;")

    class OnHeaderDecodedListener(JavaInterface, metaclass=MetaJavaClass):
        __javaclass__ = "android/graphics/ImageDecoder/OnHeaderDecodedListener"
        onHeaderDecoded = JavaMethod("(Landroid/graphics/ImageDecoder;Landroid/graphics/ImageDecoder$ImageInfo;Landroid/graphics/ImageDecoder$Source;)V")

    class OnPartialImageListener(JavaInterface, metaclass=MetaJavaClass):
        __javaclass__ = "android/graphics/ImageDecoder/OnPartialImageListener"
        onPartialImage = JavaMethod("(Landroid/graphics/ImageDecoder$DecodeException;)Z")

    class Source(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/graphics/ImageDecoder/Source"