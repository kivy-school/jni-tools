from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["NinePatch"]

class NinePatch(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/graphics/NinePatch"
    __javaconstructor__ = [("(Landroid/graphics/Bitmap;[B)V", False), ("(Landroid/graphics/Bitmap;[BLjava/lang/String;)V", False)]
    getBitmap = JavaMethod("()Landroid/graphics/Bitmap;")
    isNinePatchChunk = JavaStaticMethod("([B)Z")
    setPaint = JavaMethod("(Landroid/graphics/Paint;)V")
    getName = JavaMethod("()Ljava/lang/String;")
    hasAlpha = JavaMethod("()Z")
    getDensity = JavaMethod("()I")
    draw = JavaMultipleMethod([("(Landroid/graphics/Canvas;Landroid/graphics/Rect;Landroid/graphics/Paint;)V", False, False), ("(Landroid/graphics/Canvas;Landroid/graphics/RectF;)V", False, False), ("(Landroid/graphics/Canvas;Landroid/graphics/Rect;)V", False, False)])
    getHeight = JavaMethod("()I")
    getWidth = JavaMethod("()I")
    getPaint = JavaMethod("()Landroid/graphics/Paint;")
    getTransparentRegion = JavaMethod("(Landroid/graphics/Rect;)Landroid/graphics/Region;")