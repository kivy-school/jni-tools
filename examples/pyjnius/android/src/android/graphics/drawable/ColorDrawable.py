from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ColorDrawable"]

class ColorDrawable(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/graphics/drawable/ColorDrawable"
    __javaconstructor__ = [("()V", False), ("(I)V", False)]
    inflate = JavaMethod("(Landroid/content/res/Resources;Lorg/xmlpull/v1/XmlPullParser;Landroid/util/AttributeSet;Landroid/content/res/Resources$Theme;)V")
    setAlpha = JavaMethod("(I)V")
    setColorFilter = JavaMethod("(Landroid/graphics/ColorFilter;)V")
    getColorFilter = JavaMethod("()Landroid/graphics/ColorFilter;")
    draw = JavaMethod("(Landroid/graphics/Canvas;)V")
    getAlpha = JavaMethod("()I")
    setColor = JavaMethod("(I)V")
    getColor = JavaMethod("()I")
    getChangingConfigurations = JavaMethod("()I")
    canApplyTheme = JavaMethod("()Z")
    applyTheme = JavaMethod("(Landroid/content/res/Resources$Theme;)V")
    getConstantState = JavaMethod("()Landroid/graphics/drawable/Drawable$ConstantState;")
    getOpacity = JavaMethod("()I")
    getOutline = JavaMethod("(Landroid/graphics/Outline;)V")
    hasFocusStateSpecified = JavaMethod("()Z")
    isStateful = JavaMethod("()Z")
    mutate = JavaMethod("()Landroid/graphics/drawable/Drawable;")
    setTintBlendMode = JavaMethod("(Landroid/graphics/BlendMode;)V")
    setTintList = JavaMethod("(Landroid/content/res/ColorStateList;)V")