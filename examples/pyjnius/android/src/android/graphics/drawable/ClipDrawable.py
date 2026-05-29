from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ClipDrawable"]

class ClipDrawable(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/graphics/drawable/ClipDrawable"
    __javaconstructor__ = [("(Landroid/graphics/drawable/Drawable;II)V", False)]
    HORIZONTAL = JavaStaticField("I")
    VERTICAL = JavaStaticField("I")
    inflate = JavaMethod("(Landroid/content/res/Resources;Lorg/xmlpull/v1/XmlPullParser;Landroid/util/AttributeSet;Landroid/content/res/Resources$Theme;)V")
    draw = JavaMethod("(Landroid/graphics/Canvas;)V")
    applyTheme = JavaMethod("(Landroid/content/res/Resources$Theme;)V")
    getOpacity = JavaMethod("()I")