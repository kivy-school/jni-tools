from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["RadioButton"]

class RadioButton(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/widget/RadioButton"
    __javaconstructor__ = [("(Landroid/content/Context;)V", False), ("(Landroid/content/Context;Landroid/util/AttributeSet;)V", False), ("(Landroid/content/Context;Landroid/util/AttributeSet;I)V", False), ("(Landroid/content/Context;Landroid/util/AttributeSet;II)V", False)]
    toggle = JavaMethod("()V")
    getAccessibilityClassName = JavaMethod("()Ljava/lang/CharSequence;")
    onInitializeAccessibilityNodeInfo = JavaMethod("(Landroid/view/accessibility/AccessibilityNodeInfo;)V")