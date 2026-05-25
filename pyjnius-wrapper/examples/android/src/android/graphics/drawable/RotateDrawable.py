from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["RotateDrawable"]

class RotateDrawable(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/graphics/drawable/RotateDrawable"
    __javaconstructor__ = [("()V", False)]
    inflate = JavaMethod("(Landroid/content/res/Resources;Lorg/xmlpull/v1/XmlPullParser;Landroid/util/AttributeSet;Landroid/content/res/Resources$Theme;)V")
    applyTheme = JavaMethod("(Landroid/content/res/Resources$Theme;)V")
    draw = JavaMethod("(Landroid/graphics/Canvas;)V")
    setFromDegrees = JavaMethod("(F)V")
    getFromDegrees = JavaMethod("()F")
    setToDegrees = JavaMethod("(F)V")
    getToDegrees = JavaMethod("()F")
    setPivotX = JavaMethod("(F)V")
    getPivotX = JavaMethod("()F")
    setPivotXRelative = JavaMethod("(Z)V")
    isPivotXRelative = JavaMethod("()Z")
    setPivotY = JavaMethod("(F)V")
    getPivotY = JavaMethod("()F")
    setPivotYRelative = JavaMethod("(Z)V")
    isPivotYRelative = JavaMethod("()Z")
    onLevelChange = JavaMethod("(I)Z")