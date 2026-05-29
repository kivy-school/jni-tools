from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AnimatedVectorDrawable"]

class AnimatedVectorDrawable(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/graphics/drawable/AnimatedVectorDrawable"
    __javaconstructor__ = [("()V", False)]
    clearAnimationCallbacks = JavaMethod("()V")
    registerAnimationCallback = JavaMethod("(Landroid/graphics/drawable/Animatable2$AnimationCallback;)V")
    unregisterAnimationCallback = JavaMethod("(Landroid/graphics/drawable/Animatable2$AnimationCallback;)Z")
    reset = JavaMethod("()V")
    inflate = JavaMethod("(Landroid/content/res/Resources;Lorg/xmlpull/v1/XmlPullParser;Landroid/util/AttributeSet;Landroid/content/res/Resources$Theme;)V")
    start = JavaMethod("()V")
    setAlpha = JavaMethod("(I)V")
    setColorFilter = JavaMethod("(Landroid/graphics/ColorFilter;)V")
    getColorFilter = JavaMethod("()Landroid/graphics/ColorFilter;")
    draw = JavaMethod("(Landroid/graphics/Canvas;)V")
    getAlpha = JavaMethod("()I")
    getChangingConfigurations = JavaMethod("()I")
    stop = JavaMethod("()V")
    isRunning = JavaMethod("()Z")
    canApplyTheme = JavaMethod("()Z")
    applyTheme = JavaMethod("(Landroid/content/res/Resources$Theme;)V")
    getConstantState = JavaMethod("()Landroid/graphics/drawable/Drawable$ConstantState;")
    getIntrinsicHeight = JavaMethod("()I")
    getIntrinsicWidth = JavaMethod("()I")
    getOpacity = JavaMethod("()I")
    getOpticalInsets = JavaMethod("()Landroid/graphics/Insets;")
    getOutline = JavaMethod("(Landroid/graphics/Outline;)V")
    isStateful = JavaMethod("()Z")
    mutate = JavaMethod("()Landroid/graphics/drawable/Drawable;")
    onLayoutDirectionChanged = JavaMethod("(I)Z")
    setHotspot = JavaMethod("(FF)V")
    setHotspotBounds = JavaMethod("(IIII)V")
    setTintBlendMode = JavaMethod("(Landroid/graphics/BlendMode;)V")
    setTintList = JavaMethod("(Landroid/content/res/ColorStateList;)V")
    setVisible = JavaMethod("(ZZ)Z")