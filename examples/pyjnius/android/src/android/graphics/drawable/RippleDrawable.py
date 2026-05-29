from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["RippleDrawable"]

class RippleDrawable(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/graphics/drawable/RippleDrawable"
    __javaconstructor__ = [("(Landroid/content/res/ColorStateList;Landroid/graphics/drawable/Drawable;Landroid/graphics/drawable/Drawable;)V", False)]
    RADIUS_AUTO = JavaStaticField("I")
    jumpToCurrentState = JavaMethod("()V")
    getOpacity = JavaMethod("()I")
    onStateChange = JavaMethod("([I)Z")
    onBoundsChange = JavaMethod("(Landroid/graphics/Rect;)V")
    setVisible = JavaMethod("(ZZ)Z")
    isProjected = JavaMethod("()Z")
    isStateful = JavaMethod("()Z")
    hasFocusStateSpecified = JavaMethod("()Z")
    setColor = JavaMethod("(Landroid/content/res/ColorStateList;)V")
    setEffectColor = JavaMethod("(Landroid/content/res/ColorStateList;)V")
    getEffectColor = JavaMethod("()Landroid/content/res/ColorStateList;")
    setRadius = JavaMethod("(I)V")
    getRadius = JavaMethod("()I")
    inflate = JavaMethod("(Landroid/content/res/Resources;Lorg/xmlpull/v1/XmlPullParser;Landroid/util/AttributeSet;Landroid/content/res/Resources$Theme;)V")
    setDrawableByLayerId = JavaMethod("(ILandroid/graphics/drawable/Drawable;)Z")
    setPaddingMode = JavaMethod("(I)V")
    applyTheme = JavaMethod("(Landroid/content/res/Resources$Theme;)V")
    canApplyTheme = JavaMethod("()Z")
    setHotspot = JavaMethod("(FF)V")
    setHotspotBounds = JavaMethod("(IIII)V")
    getHotspotBounds = JavaMethod("(Landroid/graphics/Rect;)V")
    getOutline = JavaMethod("(Landroid/graphics/Outline;)V")
    draw = JavaMethod("(Landroid/graphics/Canvas;)V")
    invalidateSelf = JavaMethod("()V")
    getDirtyBounds = JavaMethod("()Landroid/graphics/Rect;")
    getConstantState = JavaMethod("()Landroid/graphics/drawable/Drawable$ConstantState;")
    mutate = JavaMethod("()Landroid/graphics/drawable/Drawable;")