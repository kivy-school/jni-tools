from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AnimatedImageDrawable"]

class AnimatedImageDrawable(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/graphics/drawable/AnimatedImageDrawable"
    __javaconstructor__ = [("()V", False)]
    REPEAT_INFINITE = JavaStaticField("I")
    clearAnimationCallbacks = JavaMethod("()V")
    registerAnimationCallback = JavaMethod("(Landroid/graphics/drawable/Animatable2$AnimationCallback;)V")
    unregisterAnimationCallback = JavaMethod("(Landroid/graphics/drawable/Animatable2$AnimationCallback;)Z")
    inflate = JavaMethod("(Landroid/content/res/Resources;Lorg/xmlpull/v1/XmlPullParser;Landroid/util/AttributeSet;Landroid/content/res/Resources$Theme;)V")
    start = JavaMethod("()V")
    setAlpha = JavaMethod("(I)V")
    setColorFilter = JavaMethod("(Landroid/graphics/ColorFilter;)V")
    getColorFilter = JavaMethod("()Landroid/graphics/ColorFilter;")
    draw = JavaMethod("(Landroid/graphics/Canvas;)V")
    getAlpha = JavaMethod("()I")
    setRepeatCount = JavaMethod("(I)V")
    stop = JavaMethod("()V")
    isRunning = JavaMethod("()Z")
    getRepeatCount = JavaMethod("()I")
    getIntrinsicHeight = JavaMethod("()I")
    getIntrinsicWidth = JavaMethod("()I")
    getOpacity = JavaMethod("()I")
    isAutoMirrored = JavaMethod("()Z")
    isFilterBitmap = JavaMethod("()Z")
    onLayoutDirectionChanged = JavaMethod("(I)Z")
    setAutoMirrored = JavaMethod("(Z)V")
    setFilterBitmap = JavaMethod("(Z)V")