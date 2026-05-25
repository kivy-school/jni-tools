from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["VectorDrawable"]

class VectorDrawable(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/graphics/drawable/VectorDrawable"
    __javaconstructor__ = [("()V", False)]
    mutate = JavaMethod("()Landroid/graphics/drawable/Drawable;")
    getConstantState = JavaMethod("()Landroid/graphics/drawable/Drawable$ConstantState;")
    draw = JavaMethod("(Landroid/graphics/Canvas;)V")
    getAlpha = JavaMethod("()I")
    setAlpha = JavaMethod("(I)V")
    setColorFilter = JavaMethod("(Landroid/graphics/ColorFilter;)V")
    getColorFilter = JavaMethod("()Landroid/graphics/ColorFilter;")
    setTintList = JavaMethod("(Landroid/content/res/ColorStateList;)V")
    setTintBlendMode = JavaMethod("(Landroid/graphics/BlendMode;)V")
    isStateful = JavaMethod("()Z")
    hasFocusStateSpecified = JavaMethod("()Z")
    onStateChange = JavaMethod("([I)Z")
    getOpacity = JavaMethod("()I")
    getIntrinsicWidth = JavaMethod("()I")
    getIntrinsicHeight = JavaMethod("()I")
    getOpticalInsets = JavaMethod("()Landroid/graphics/Insets;")
    canApplyTheme = JavaMethod("()Z")
    applyTheme = JavaMethod("(Landroid/content/res/Resources$Theme;)V")
    inflate = JavaMethod("(Landroid/content/res/Resources;Lorg/xmlpull/v1/XmlPullParser;Landroid/util/AttributeSet;Landroid/content/res/Resources$Theme;)V")
    getChangingConfigurations = JavaMethod("()I")
    setAutoMirrored = JavaMethod("(Z)V")
    isAutoMirrored = JavaMethod("()Z")