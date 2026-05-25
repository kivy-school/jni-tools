from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AnimatedStateListDrawable"]

class AnimatedStateListDrawable(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/graphics/drawable/AnimatedStateListDrawable"
    __javaconstructor__ = [("()V", False)]
    setVisible = JavaMethod("(ZZ)Z")
    addState = JavaMethod("([ILandroid/graphics/drawable/Drawable;I)V")
    addTransition = JavaMethod("(IILandroid/graphics/drawable/Drawable;Z)V")
    isStateful = JavaMethod("()Z")
    onStateChange = JavaMethod("([I)Z")
    jumpToCurrentState = JavaMethod("()V")
    inflate = JavaMethod("(Landroid/content/res/Resources;Lorg/xmlpull/v1/XmlPullParser;Landroid/util/AttributeSet;Landroid/content/res/Resources$Theme;)V")
    applyTheme = JavaMethod("(Landroid/content/res/Resources$Theme;)V")
    mutate = JavaMethod("()Landroid/graphics/drawable/Drawable;")
    setConstantState = JavaMethod("(Landroid/graphics/drawable/DrawableContainer$DrawableContainerState;)V")