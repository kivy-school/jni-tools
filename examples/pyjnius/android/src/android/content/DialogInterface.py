from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["DialogInterface"]

class DialogInterface(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "android/content/DialogInterface"
    BUTTON1 = JavaStaticField("I")
    BUTTON2 = JavaStaticField("I")
    BUTTON3 = JavaStaticField("I")
    BUTTON_NEGATIVE = JavaStaticField("I")
    BUTTON_NEUTRAL = JavaStaticField("I")
    BUTTON_POSITIVE = JavaStaticField("I")
    cancel = JavaMethod("()V")
    dismiss = JavaMethod("()V")

    class OnCancelListener(JavaInterface, metaclass=MetaJavaClass):
        __javaclass__ = "android/content/DialogInterface/OnCancelListener"
        onCancel = JavaMethod("(Landroid/content/DialogInterface;)V")

    class OnClickListener(JavaInterface, metaclass=MetaJavaClass):
        __javaclass__ = "android/content/DialogInterface/OnClickListener"
        onClick = JavaMethod("(Landroid/content/DialogInterface;I)V")

    class OnDismissListener(JavaInterface, metaclass=MetaJavaClass):
        __javaclass__ = "android/content/DialogInterface/OnDismissListener"
        onDismiss = JavaMethod("(Landroid/content/DialogInterface;)V")

    class OnKeyListener(JavaInterface, metaclass=MetaJavaClass):
        __javaclass__ = "android/content/DialogInterface/OnKeyListener"
        onKey = JavaMethod("(Landroid/content/DialogInterface;ILandroid/view/KeyEvent;)Z")

    class OnMultiChoiceClickListener(JavaInterface, metaclass=MetaJavaClass):
        __javaclass__ = "android/content/DialogInterface/OnMultiChoiceClickListener"
        onClick = JavaMethod("(Landroid/content/DialogInterface;IZ)V")

    class OnShowListener(JavaInterface, metaclass=MetaJavaClass):
        __javaclass__ = "android/content/DialogInterface/OnShowListener"
        onShow = JavaMethod("(Landroid/content/DialogInterface;)V")