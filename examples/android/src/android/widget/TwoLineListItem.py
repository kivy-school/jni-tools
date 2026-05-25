from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["TwoLineListItem"]

class TwoLineListItem(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/widget/TwoLineListItem"
    __javaconstructor__ = [("(Landroid/content/Context;)V", False), ("(Landroid/content/Context;Landroid/util/AttributeSet;)V", False), ("(Landroid/content/Context;Landroid/util/AttributeSet;I)V", False), ("(Landroid/content/Context;Landroid/util/AttributeSet;II)V", False)]
    onFinishInflate = JavaMethod("()V")
    getText1 = JavaMethod("()Landroid/widget/TextView;")
    getText2 = JavaMethod("()Landroid/widget/TextView;")
    getAccessibilityClassName = JavaMethod("()Ljava/lang/CharSequence;")