from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["InsetDrawable"]

class InsetDrawable(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/graphics/drawable/InsetDrawable"
    __javaconstructor__ = [("(Landroid/graphics/drawable/Drawable;I)V", False), ("(Landroid/graphics/drawable/Drawable;F)V", False), ("(Landroid/graphics/drawable/Drawable;IIII)V", False), ("(Landroid/graphics/drawable/Drawable;FFFF)V", False)]
    inflate = JavaMethod("(Landroid/content/res/Resources;Lorg/xmlpull/v1/XmlPullParser;Landroid/util/AttributeSet;Landroid/content/res/Resources$Theme;)V")
    applyTheme = JavaMethod("(Landroid/content/res/Resources$Theme;)V")
    getPadding = JavaMethod("(Landroid/graphics/Rect;)Z")
    getOpticalInsets = JavaMethod("()Landroid/graphics/Insets;")
    getOpacity = JavaMethod("()I")
    onBoundsChange = JavaMethod("(Landroid/graphics/Rect;)V")
    getIntrinsicWidth = JavaMethod("()I")
    getIntrinsicHeight = JavaMethod("()I")
    getOutline = JavaMethod("(Landroid/graphics/Outline;)V")