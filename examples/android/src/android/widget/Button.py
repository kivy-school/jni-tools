from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Button"]

class Button(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/widget/Button"
    __javaconstructor__ = [("(Landroid/content/Context;)V", False), ("(Landroid/content/Context;Landroid/util/AttributeSet;)V", False), ("(Landroid/content/Context;Landroid/util/AttributeSet;I)V", False), ("(Landroid/content/Context;Landroid/util/AttributeSet;II)V", False)]
    getAccessibilityClassName = JavaMethod("()Ljava/lang/CharSequence;")
    onResolvePointerIcon = JavaMethod("(Landroid/view/MotionEvent;I)Landroid/view/PointerIcon;")