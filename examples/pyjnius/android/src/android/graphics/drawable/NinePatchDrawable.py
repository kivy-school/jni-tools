from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["NinePatchDrawable"]

class NinePatchDrawable(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/graphics/drawable/NinePatchDrawable"
    __javaconstructor__ = [("(Landroid/graphics/Bitmap;[BLandroid/graphics/Rect;Ljava/lang/String;)V", False), ("(Landroid/content/res/Resources;Landroid/graphics/Bitmap;[BLandroid/graphics/Rect;Ljava/lang/String;)V", False), ("(Landroid/graphics/NinePatch;)V", False), ("(Landroid/content/res/Resources;Landroid/graphics/NinePatch;)V", False)]
    setTargetDensity = JavaMultipleMethod([("(Landroid/graphics/Canvas;)V", False, False), ("(Landroid/util/DisplayMetrics;)V", False, False), ("(I)V", False, False)])
    draw = JavaMethod("(Landroid/graphics/Canvas;)V")
    getChangingConfigurations = JavaMethod("()I")
    getPadding = JavaMethod("(Landroid/graphics/Rect;)Z")
    getOutline = JavaMethod("(Landroid/graphics/Outline;)V")
    getOpticalInsets = JavaMethod("()Landroid/graphics/Insets;")
    setAlpha = JavaMethod("(I)V")
    getAlpha = JavaMethod("()I")
    setColorFilter = JavaMethod("(Landroid/graphics/ColorFilter;)V")
    setTintList = JavaMethod("(Landroid/content/res/ColorStateList;)V")
    setTintBlendMode = JavaMethod("(Landroid/graphics/BlendMode;)V")
    setDither = JavaMethod("(Z)V")
    setAutoMirrored = JavaMethod("(Z)V")
    isAutoMirrored = JavaMethod("()Z")
    setFilterBitmap = JavaMethod("(Z)V")
    isFilterBitmap = JavaMethod("()Z")
    inflate = JavaMethod("(Landroid/content/res/Resources;Lorg/xmlpull/v1/XmlPullParser;Landroid/util/AttributeSet;Landroid/content/res/Resources$Theme;)V")
    applyTheme = JavaMethod("(Landroid/content/res/Resources$Theme;)V")
    canApplyTheme = JavaMethod("()Z")
    getPaint = JavaMethod("()Landroid/graphics/Paint;")
    getIntrinsicWidth = JavaMethod("()I")
    getIntrinsicHeight = JavaMethod("()I")
    getOpacity = JavaMethod("()I")
    getTransparentRegion = JavaMethod("()Landroid/graphics/Region;")
    getConstantState = JavaMethod("()Landroid/graphics/drawable/Drawable$ConstantState;")
    mutate = JavaMethod("()Landroid/graphics/drawable/Drawable;")
    onStateChange = JavaMethod("([I)Z")
    isStateful = JavaMethod("()Z")
    hasFocusStateSpecified = JavaMethod("()Z")