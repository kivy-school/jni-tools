from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["PaintDrawable"]

class PaintDrawable(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/graphics/drawable/PaintDrawable"
    __javaconstructor__ = [("()V", False), ("(I)V", False)]
    setCornerRadius = JavaMethod("(F)V")
    setCornerRadii = JavaMethod("([F)V")
    inflateTag = JavaMethod("(Ljava/lang/String;Landroid/content/res/Resources;Lorg/xmlpull/v1/XmlPullParser;Landroid/util/AttributeSet;)Z")