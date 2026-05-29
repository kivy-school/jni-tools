from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["VectorDrawable"]

class VectorDrawable(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/graphics/drawable/VectorDrawable"
    __javaconstructor__ = [("()V", False)]
    inflate = JavaMethod("(Landroid/content/res/Resources;Lorg/xmlpull/v1/XmlPullParser;Landroid/util/AttributeSet;Landroid/content/res/Resources$Theme;)V")
    setAlpha = JavaMethod("(I)V")
    setColorFilter = JavaMethod("(Landroid/graphics/ColorFilter;)V")
    getColorFilter = JavaMethod("()Landroid/graphics/ColorFilter;")
    draw = JavaMethod("(Landroid/graphics/Canvas;)V")
    getAlpha = JavaMethod("()I")
    getChangingConfigurations = JavaMethod("()I")
    canApplyTheme = JavaMethod("()Z")
    applyTheme = JavaMethod("(Landroid/content/res/Resources$Theme;)V")
    getConstantState = JavaMethod("()Landroid/graphics/drawable/Drawable$ConstantState;")
    getIntrinsicHeight = JavaMethod("()I")
    getIntrinsicWidth = JavaMethod("()I")
    getOpacity = JavaMethod("()I")
    getOpticalInsets = JavaMethod("()Landroid/graphics/Insets;")
    hasFocusStateSpecified = JavaMethod("()Z")
    isAutoMirrored = JavaMethod("()Z")
    isStateful = JavaMethod("()Z")
    mutate = JavaMethod("()Landroid/graphics/drawable/Drawable;")
    setAutoMirrored = JavaMethod("(Z)V")
    setTintBlendMode = JavaMethod("(Landroid/graphics/BlendMode;)V")
    setTintList = JavaMethod("(Landroid/content/res/ColorStateList;)V")