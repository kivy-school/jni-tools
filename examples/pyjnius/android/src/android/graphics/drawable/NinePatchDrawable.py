from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["NinePatchDrawable"]

class NinePatchDrawable(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/graphics/drawable/NinePatchDrawable"
    __javaconstructor__ = [("(Landroid/content/res/Resources;Landroid/graphics/Bitmap;[BLandroid/graphics/Rect;Ljava/lang/String;)V", False), ("(Landroid/content/res/Resources;Landroid/graphics/NinePatch;)V", False), ("(Landroid/graphics/Bitmap;[BLandroid/graphics/Rect;Ljava/lang/String;)V", False), ("(Landroid/graphics/NinePatch;)V", False)]
    setTargetDensity = JavaMultipleMethod([("(Landroid/util/DisplayMetrics;)V", False, False), ("(I)V", False, False), ("(Landroid/graphics/Canvas;)V", False, False)])
    inflate = JavaMethod("(Landroid/content/res/Resources;Lorg/xmlpull/v1/XmlPullParser;Landroid/util/AttributeSet;Landroid/content/res/Resources$Theme;)V")
    setAlpha = JavaMethod("(I)V")
    setColorFilter = JavaMethod("(Landroid/graphics/ColorFilter;)V")
    draw = JavaMethod("(Landroid/graphics/Canvas;)V")
    getAlpha = JavaMethod("()I")
    getPaint = JavaMethod("()Landroid/graphics/Paint;")
    getChangingConfigurations = JavaMethod("()I")
    canApplyTheme = JavaMethod("()Z")
    applyTheme = JavaMethod("(Landroid/content/res/Resources$Theme;)V")
    getConstantState = JavaMethod("()Landroid/graphics/drawable/Drawable$ConstantState;")
    getIntrinsicHeight = JavaMethod("()I")
    getIntrinsicWidth = JavaMethod("()I")
    getOpacity = JavaMethod("()I")
    getOpticalInsets = JavaMethod("()Landroid/graphics/Insets;")
    getOutline = JavaMethod("(Landroid/graphics/Outline;)V")
    getPadding = JavaMethod("(Landroid/graphics/Rect;)Z")
    getTransparentRegion = JavaMethod("()Landroid/graphics/Region;")
    hasFocusStateSpecified = JavaMethod("()Z")
    isAutoMirrored = JavaMethod("()Z")
    isFilterBitmap = JavaMethod("()Z")
    isStateful = JavaMethod("()Z")
    mutate = JavaMethod("()Landroid/graphics/drawable/Drawable;")
    setAutoMirrored = JavaMethod("(Z)V")
    setDither = JavaMethod("(Z)V")
    setFilterBitmap = JavaMethod("(Z)V")
    setTintBlendMode = JavaMethod("(Landroid/graphics/BlendMode;)V")
    setTintList = JavaMethod("(Landroid/content/res/ColorStateList;)V")