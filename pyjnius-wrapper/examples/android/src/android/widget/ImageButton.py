from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ImageButton"]

class ImageButton(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/widget/ImageButton"
    __javaconstructor__ = [("(Landroid/content/Context;)V", False), ("(Landroid/content/Context;Landroid/util/AttributeSet;)V", False), ("(Landroid/content/Context;Landroid/util/AttributeSet;I)V", False), ("(Landroid/content/Context;Landroid/util/AttributeSet;II)V", False)]
    onSetAlpha = JavaMethod("(I)Z")
    getAccessibilityClassName = JavaMethod("()Ljava/lang/CharSequence;")
    onResolvePointerIcon = JavaMethod("(Landroid/view/MotionEvent;I)Landroid/view/PointerIcon;")