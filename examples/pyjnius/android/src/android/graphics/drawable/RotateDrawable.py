from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["RotateDrawable"]

class RotateDrawable(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/graphics/drawable/RotateDrawable"
    __javaconstructor__ = [("()V", False)]
    setPivotXRelative = JavaMethod("(Z)V")
    setFromDegrees = JavaMethod("(F)V")
    isPivotYRelative = JavaMethod("()Z")
    getToDegrees = JavaMethod("()F")
    setPivotYRelative = JavaMethod("(Z)V")
    isPivotXRelative = JavaMethod("()Z")
    setToDegrees = JavaMethod("(F)V")
    getFromDegrees = JavaMethod("()F")
    inflate = JavaMethod("(Landroid/content/res/Resources;Lorg/xmlpull/v1/XmlPullParser;Landroid/util/AttributeSet;Landroid/content/res/Resources$Theme;)V")
    draw = JavaMethod("(Landroid/graphics/Canvas;)V")
    getPivotX = JavaMethod("()F")
    getPivotY = JavaMethod("()F")
    setPivotX = JavaMethod("(F)V")
    setPivotY = JavaMethod("(F)V")
    applyTheme = JavaMethod("(Landroid/content/res/Resources$Theme;)V")