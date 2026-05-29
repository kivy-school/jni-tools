from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AnimatedStateListDrawable"]

class AnimatedStateListDrawable(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/graphics/drawable/AnimatedStateListDrawable"
    __javaconstructor__ = [("()V", False)]
    addState = JavaMethod("([ILandroid/graphics/drawable/Drawable;I)V")
    addTransition = JavaMethod("(IILandroid/graphics/drawable/Drawable;Z)V")
    inflate = JavaMethod("(Landroid/content/res/Resources;Lorg/xmlpull/v1/XmlPullParser;Landroid/util/AttributeSet;Landroid/content/res/Resources$Theme;)V")
    applyTheme = JavaMethod("(Landroid/content/res/Resources$Theme;)V")
    isStateful = JavaMethod("()Z")
    jumpToCurrentState = JavaMethod("()V")
    mutate = JavaMethod("()Landroid/graphics/drawable/Drawable;")
    setVisible = JavaMethod("(ZZ)Z")