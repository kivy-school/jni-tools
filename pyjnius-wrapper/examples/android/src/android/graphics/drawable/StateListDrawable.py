from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["StateListDrawable"]

class StateListDrawable(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/graphics/drawable/StateListDrawable"
    __javaconstructor__ = [("()V", False)]
    addState = JavaMethod("([ILandroid/graphics/drawable/Drawable;)V")
    isStateful = JavaMethod("()Z")
    hasFocusStateSpecified = JavaMethod("()Z")
    onStateChange = JavaMethod("([I)Z")
    inflate = JavaMethod("(Landroid/content/res/Resources;Lorg/xmlpull/v1/XmlPullParser;Landroid/util/AttributeSet;Landroid/content/res/Resources$Theme;)V")
    getStateCount = JavaMethod("()I")
    getStateSet = JavaMethod("(I)[I")
    getStateDrawable = JavaMethod("(I)Landroid/graphics/drawable/Drawable;")
    findStateDrawableIndex = JavaMethod("([I)I")
    mutate = JavaMethod("()Landroid/graphics/drawable/Drawable;")
    applyTheme = JavaMethod("(Landroid/content/res/Resources$Theme;)V")
    setConstantState = JavaMethod("(Landroid/graphics/drawable/DrawableContainer$DrawableContainerState;)V")