from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["TransformationMethod"]

class TransformationMethod(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "android/text/method/TransformationMethod"
    getTransformation = JavaMethod("(Ljava/lang/CharSequence;Landroid/view/View;)Ljava/lang/CharSequence;")
    onFocusChanged = JavaMethod("(Landroid/view/View;Ljava/lang/CharSequence;ZILandroid/graphics/Rect;)V")