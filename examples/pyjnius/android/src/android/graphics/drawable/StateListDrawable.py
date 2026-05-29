from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["StateListDrawable"]

class StateListDrawable(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/graphics/drawable/StateListDrawable"
    __javaconstructor__ = [("()V", False)]
    addState = JavaMethod("([ILandroid/graphics/drawable/Drawable;)V")
    getStateSet = JavaMethod("(I)[I")
    getStateDrawable = JavaMethod("(I)Landroid/graphics/drawable/Drawable;")
    getStateCount = JavaMethod("()I")
    findStateDrawableIndex = JavaMethod("([I)I")
    inflate = JavaMethod("(Landroid/content/res/Resources;Lorg/xmlpull/v1/XmlPullParser;Landroid/util/AttributeSet;Landroid/content/res/Resources$Theme;)V")
    applyTheme = JavaMethod("(Landroid/content/res/Resources$Theme;)V")
    hasFocusStateSpecified = JavaMethod("()Z")
    isStateful = JavaMethod("()Z")
    mutate = JavaMethod("()Landroid/graphics/drawable/Drawable;")