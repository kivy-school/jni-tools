from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AnimatedImageDrawable"]

class AnimatedImageDrawable(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/graphics/drawable/AnimatedImageDrawable"
    __javaconstructor__ = [("()V", False)]
    REPEAT_INFINITE = JavaStaticField("I")
    setRepeatCount = JavaMethod("(I)V")
    getRepeatCount = JavaMethod("()I")
    inflate = JavaMethod("(Landroid/content/res/Resources;Lorg/xmlpull/v1/XmlPullParser;Landroid/util/AttributeSet;Landroid/content/res/Resources$Theme;)V")
    getIntrinsicWidth = JavaMethod("()I")
    getIntrinsicHeight = JavaMethod("()I")
    draw = JavaMethod("(Landroid/graphics/Canvas;)V")
    setAlpha = JavaMethod("(I)V")
    getAlpha = JavaMethod("()I")
    setColorFilter = JavaMethod("(Landroid/graphics/ColorFilter;)V")
    getColorFilter = JavaMethod("()Landroid/graphics/ColorFilter;")
    getOpacity = JavaMethod("()I")
    setAutoMirrored = JavaMethod("(Z)V")
    onLayoutDirectionChanged = JavaMethod("(I)Z")
    isAutoMirrored = JavaMethod("()Z")
    isRunning = JavaMethod("()Z")
    start = JavaMethod("()V")
    stop = JavaMethod("()V")
    registerAnimationCallback = JavaMethod("(Landroid/graphics/drawable/Animatable2$AnimationCallback;)V")
    unregisterAnimationCallback = JavaMethod("(Landroid/graphics/drawable/Animatable2$AnimationCallback;)Z")
    clearAnimationCallbacks = JavaMethod("()V")
    onBoundsChange = JavaMethod("(Landroid/graphics/Rect;)V")