from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ReplacementTransformationMethod"]

class ReplacementTransformationMethod(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/text/method/ReplacementTransformationMethod"
    __javaconstructor__ = [("()V", False)]
    onFocusChanged = JavaMethod("(Landroid/view/View;Ljava/lang/CharSequence;ZILandroid/graphics/Rect;)V")
    getTransformation = JavaMethod("(Ljava/lang/CharSequence;Landroid/view/View;)Ljava/lang/CharSequence;")