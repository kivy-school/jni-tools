from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ScaleDrawable"]

class ScaleDrawable(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/graphics/drawable/ScaleDrawable"
    __javaconstructor__ = [("(Landroid/graphics/drawable/Drawable;IFF)V", False)]
    inflate = JavaMethod("(Landroid/content/res/Resources;Lorg/xmlpull/v1/XmlPullParser;Landroid/util/AttributeSet;Landroid/content/res/Resources$Theme;)V")
    applyTheme = JavaMethod("(Landroid/content/res/Resources$Theme;)V")
    draw = JavaMethod("(Landroid/graphics/Canvas;)V")
    getOpacity = JavaMethod("()I")
    onLevelChange = JavaMethod("(I)Z")
    onBoundsChange = JavaMethod("(Landroid/graphics/Rect;)V")