from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["TextureView"]

class TextureView(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/view/TextureView"
    __javaconstructor__ = [("(Landroid/content/Context;)V", False), ("(Landroid/content/Context;Landroid/util/AttributeSet;)V", False), ("(Landroid/content/Context;Landroid/util/AttributeSet;I)V", False), ("(Landroid/content/Context;Landroid/util/AttributeSet;II)V", False)]
    isOpaque = JavaMethod("()Z")
    setOpaque = JavaMethod("(Z)V")
    onAttachedToWindow = JavaMethod("()V")
    setLayerType = JavaMethod("(ILandroid/graphics/Paint;)V")
    setLayerPaint = JavaMethod("(Landroid/graphics/Paint;)V")
    getLayerType = JavaMethod("()I")
    buildLayer = JavaMethod("()V")
    setForeground = JavaMethod("(Landroid/graphics/drawable/Drawable;)V")
    setBackgroundDrawable = JavaMethod("(Landroid/graphics/drawable/Drawable;)V")
    draw = JavaMethod("(Landroid/graphics/Canvas;)V")
    onDraw = JavaMethod("(Landroid/graphics/Canvas;)V")
    onSizeChanged = JavaMethod("(IIII)V")
    onVisibilityChanged = JavaMethod("(Landroid/view/View;I)V")
    setTransform = JavaMethod("(Landroid/graphics/Matrix;)V")
    getTransform = JavaMethod("(Landroid/graphics/Matrix;)Landroid/graphics/Matrix;")
    getBitmap = JavaMultipleMethod([("()Landroid/graphics/Bitmap;", False, False), ("(II)Landroid/graphics/Bitmap;", False, False), ("(Landroid/graphics/Bitmap;)Landroid/graphics/Bitmap;", False, False)])
    isAvailable = JavaMethod("()Z")
    lockCanvas = JavaMultipleMethod([("()Landroid/graphics/Canvas;", False, False), ("(Landroid/graphics/Rect;)Landroid/graphics/Canvas;", False, False)])
    unlockCanvasAndPost = JavaMethod("(Landroid/graphics/Canvas;)V")
    getSurfaceTexture = JavaMethod("()Landroid/graphics/SurfaceTexture;")
    setSurfaceTexture = JavaMethod("(Landroid/graphics/SurfaceTexture;)V")
    getSurfaceTextureListener = JavaMethod("()Landroid/view/TextureView$SurfaceTextureListener;")
    setSurfaceTextureListener = JavaMethod("(Landroid/view/TextureView$SurfaceTextureListener;)V")

    class SurfaceTextureListener(JavaInterface, metaclass=MetaJavaClass):
        __javaclass__ = "android/view/TextureView/SurfaceTextureListener"
        onSurfaceTextureAvailable = JavaMethod("(Landroid/graphics/SurfaceTexture;II)V")
        onSurfaceTextureSizeChanged = JavaMethod("(Landroid/graphics/SurfaceTexture;II)V")
        onSurfaceTextureDestroyed = JavaMethod("(Landroid/graphics/SurfaceTexture;)Z")
        onSurfaceTextureUpdated = JavaMethod("(Landroid/graphics/SurfaceTexture;)V")