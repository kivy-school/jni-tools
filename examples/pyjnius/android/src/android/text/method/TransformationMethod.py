from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["TransformationMethod"]

class TransformationMethod(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/text/method/TransformationMethod"
    onFocusChanged = JavaMethod("(Landroid/view/View;Ljava/lang/CharSequence;ZILandroid/graphics/Rect;)V")
    getTransformation = JavaMethod("(Ljava/lang/CharSequence;Landroid/view/View;)Ljava/lang/CharSequence;")