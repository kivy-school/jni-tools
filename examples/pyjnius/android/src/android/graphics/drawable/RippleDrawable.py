from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["RippleDrawable"]

class RippleDrawable(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/graphics/drawable/RippleDrawable"
    __javaconstructor__ = [("(Landroid/content/res/ColorStateList;Landroid/graphics/drawable/Drawable;Landroid/graphics/drawable/Drawable;)V", False)]
    RADIUS_AUTO = JavaStaticField("I")
    INSET_UNDEFINED = JavaStaticField("I")
    PADDING_MODE_NEST = JavaStaticField("I")
    PADDING_MODE_STACK = JavaStaticField("I")
    setDrawableByLayerId = JavaMethod("(ILandroid/graphics/drawable/Drawable;)Z")
    setPaddingMode = JavaMethod("(I)V")
    setRadius = JavaMethod("(I)V")
    setEffectColor = JavaMethod("(Landroid/content/res/ColorStateList;)V")
    getEffectColor = JavaMethod("()Landroid/content/res/ColorStateList;")
    inflate = JavaMethod("(Landroid/content/res/Resources;Lorg/xmlpull/v1/XmlPullParser;Landroid/util/AttributeSet;Landroid/content/res/Resources$Theme;)V")
    draw = JavaMethod("(Landroid/graphics/Canvas;)V")
    setColor = JavaMethod("(Landroid/content/res/ColorStateList;)V")
    getRadius = JavaMethod("()I")
    canApplyTheme = JavaMethod("()Z")
    applyTheme = JavaMethod("(Landroid/content/res/Resources$Theme;)V")
    getConstantState = JavaMethod("()Landroid/graphics/drawable/Drawable$ConstantState;")
    getDirtyBounds = JavaMethod("()Landroid/graphics/Rect;")
    getHotspotBounds = JavaMethod("(Landroid/graphics/Rect;)V")
    getOpacity = JavaMethod("()I")
    getOutline = JavaMethod("(Landroid/graphics/Outline;)V")
    hasFocusStateSpecified = JavaMethod("()Z")
    invalidateSelf = JavaMethod("()V")
    isProjected = JavaMethod("()Z")
    isStateful = JavaMethod("()Z")
    jumpToCurrentState = JavaMethod("()V")
    mutate = JavaMethod("()Landroid/graphics/drawable/Drawable;")
    setHotspot = JavaMethod("(FF)V")
    setHotspotBounds = JavaMethod("(IIII)V")
    setVisible = JavaMethod("(ZZ)Z")