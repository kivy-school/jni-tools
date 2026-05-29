from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ColorDrawable"]

class ColorDrawable(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/graphics/drawable/ColorDrawable"
    __javaconstructor__ = [("()V", False), ("(I)V", False)]
    getChangingConfigurations = JavaMethod("()I")
    mutate = JavaMethod("()Landroid/graphics/drawable/Drawable;")
    draw = JavaMethod("(Landroid/graphics/Canvas;)V")
    getColor = JavaMethod("()I")
    setColor = JavaMethod("(I)V")
    getAlpha = JavaMethod("()I")
    setAlpha = JavaMethod("(I)V")
    setColorFilter = JavaMethod("(Landroid/graphics/ColorFilter;)V")
    getColorFilter = JavaMethod("()Landroid/graphics/ColorFilter;")
    setTintList = JavaMethod("(Landroid/content/res/ColorStateList;)V")
    setTintBlendMode = JavaMethod("(Landroid/graphics/BlendMode;)V")
    onStateChange = JavaMethod("([I)Z")
    isStateful = JavaMethod("()Z")
    hasFocusStateSpecified = JavaMethod("()Z")
    getOpacity = JavaMethod("()I")
    getOutline = JavaMethod("(Landroid/graphics/Outline;)V")
    inflate = JavaMethod("(Landroid/content/res/Resources;Lorg/xmlpull/v1/XmlPullParser;Landroid/util/AttributeSet;Landroid/content/res/Resources$Theme;)V")
    canApplyTheme = JavaMethod("()Z")
    applyTheme = JavaMethod("(Landroid/content/res/Resources$Theme;)V")
    getConstantState = JavaMethod("()Landroid/graphics/drawable/Drawable$ConstantState;")