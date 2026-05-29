from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["QwertyKeyListener"]

class QwertyKeyListener(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/text/method/QwertyKeyListener"
    __javaconstructor__ = [("(Landroid/text/method/TextKeyListener$Capitalize;Z)V", False)]
    META_ALT_LOCKED = JavaStaticField("I")
    META_ALT_ON = JavaStaticField("I")
    META_CAP_LOCKED = JavaStaticField("I")
    META_SHIFT_ON = JavaStaticField("I")
    META_SYM_LOCKED = JavaStaticField("I")
    META_SYM_ON = JavaStaticField("I")
    getInstanceForFullKeyboard = JavaStaticMethod("()Landroid/text/method/QwertyKeyListener;")
    markAsReplaced = JavaStaticMethod("(Landroid/text/Spannable;IILjava/lang/String;)V")
    getInstance = JavaStaticMethod("(ZLandroid/text/method/TextKeyListener$Capitalize;)Landroid/text/method/QwertyKeyListener;")
    onKeyDown = JavaMethod("(Landroid/view/View;Landroid/text/Editable;ILandroid/view/KeyEvent;)Z")
    getInputType = JavaMethod("()I")