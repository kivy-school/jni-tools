from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["InsetDrawable"]

class InsetDrawable(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/graphics/drawable/InsetDrawable"
    __javaconstructor__ = [("(Landroid/graphics/drawable/Drawable;IIII)V", False), ("(Landroid/graphics/drawable/Drawable;I)V", False), ("(Landroid/graphics/drawable/Drawable;FFFF)V", False), ("(Landroid/graphics/drawable/Drawable;F)V", False)]
    inflate = JavaMethod("(Landroid/content/res/Resources;Lorg/xmlpull/v1/XmlPullParser;Landroid/util/AttributeSet;Landroid/content/res/Resources$Theme;)V")
    applyTheme = JavaMethod("(Landroid/content/res/Resources$Theme;)V")
    getIntrinsicHeight = JavaMethod("()I")
    getIntrinsicWidth = JavaMethod("()I")
    getOpacity = JavaMethod("()I")
    getOpticalInsets = JavaMethod("()Landroid/graphics/Insets;")
    getOutline = JavaMethod("(Landroid/graphics/Outline;)V")
    getPadding = JavaMethod("(Landroid/graphics/Rect;)Z")