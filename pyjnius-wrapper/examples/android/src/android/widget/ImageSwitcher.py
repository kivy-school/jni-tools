from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ImageSwitcher"]

class ImageSwitcher(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/widget/ImageSwitcher"
    __javaconstructor__ = [("(Landroid/content/Context;)V", False), ("(Landroid/content/Context;Landroid/util/AttributeSet;)V", False)]
    setImageResource = JavaMethod("(I)V")
    setImageURI = JavaMethod("(Landroid/net/Uri;)V")
    setImageDrawable = JavaMethod("(Landroid/graphics/drawable/Drawable;)V")
    getAccessibilityClassName = JavaMethod("()Ljava/lang/CharSequence;")