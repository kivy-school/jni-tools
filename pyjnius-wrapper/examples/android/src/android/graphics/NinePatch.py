from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["NinePatch"]

class NinePatch(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/graphics/NinePatch"
    __javaconstructor__ = [("(Landroid/graphics/Bitmap;[B)V", False), ("(Landroid/graphics/Bitmap;[BLjava/lang/String;)V", False)]
    finalize = JavaMethod("()V")
    getName = JavaMethod("()Ljava/lang/String;")
    getPaint = JavaMethod("()Landroid/graphics/Paint;")
    setPaint = JavaMethod("(Landroid/graphics/Paint;)V")
    getBitmap = JavaMethod("()Landroid/graphics/Bitmap;")
    draw = JavaMultipleMethod([("(Landroid/graphics/Canvas;Landroid/graphics/RectF;)V", False, False), ("(Landroid/graphics/Canvas;Landroid/graphics/Rect;)V", False, False), ("(Landroid/graphics/Canvas;Landroid/graphics/Rect;Landroid/graphics/Paint;)V", False, False)])
    getDensity = JavaMethod("()I")
    getWidth = JavaMethod("()I")
    getHeight = JavaMethod("()I")
    hasAlpha = JavaMethod("()Z")
    getTransparentRegion = JavaMethod("(Landroid/graphics/Rect;)Landroid/graphics/Region;")
    isNinePatchChunk = JavaStaticMethod("([B)Z")