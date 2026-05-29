from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["TextKeyListener"]

class TextKeyListener(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/text/method/TextKeyListener"
    __javaconstructor__ = [("(Landroid/text/method/TextKeyListener$Capitalize;Z)V", False)]
    META_ALT_LOCKED = JavaStaticField("I")
    META_ALT_ON = JavaStaticField("I")
    META_CAP_LOCKED = JavaStaticField("I")
    META_SHIFT_ON = JavaStaticField("I")
    META_SYM_LOCKED = JavaStaticField("I")
    META_SYM_ON = JavaStaticField("I")
    shouldCap = JavaStaticMethod("(Landroid/text/method/TextKeyListener$Capitalize;Ljava/lang/CharSequence;I)Z")
    onSpanChanged = JavaMethod("(Landroid/text/Spannable;Ljava/lang/Object;IIII)V")
    onSpanRemoved = JavaMethod("(Landroid/text/Spannable;Ljava/lang/Object;II)V")
    clear = JavaStaticMethod("(Landroid/text/Editable;)V")
    getInstance = JavaMultipleMethod([("(ZLandroid/text/method/TextKeyListener$Capitalize;)Landroid/text/method/TextKeyListener;", True, False), ("()Landroid/text/method/TextKeyListener;", True, False)])
    release = JavaMethod("()V")
    onKeyDown = JavaMethod("(Landroid/view/View;Landroid/text/Editable;ILandroid/view/KeyEvent;)Z")
    onKeyUp = JavaMethod("(Landroid/view/View;Landroid/text/Editable;ILandroid/view/KeyEvent;)Z")
    getInputType = JavaMethod("()I")
    onKeyOther = JavaMethod("(Landroid/view/View;Landroid/text/Editable;Landroid/view/KeyEvent;)Z")
    onSpanAdded = JavaMethod("(Landroid/text/Spannable;Ljava/lang/Object;II)V")

    class Capitalize(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/text/method/TextKeyListener$Capitalize"
        CHARACTERS = JavaStaticField("Landroid/text/method/TextKeyListener$Capitalize;")
        NONE = JavaStaticField("Landroid/text/method/TextKeyListener$Capitalize;")
        SENTENCES = JavaStaticField("Landroid/text/method/TextKeyListener$Capitalize;")
        WORDS = JavaStaticField("Landroid/text/method/TextKeyListener$Capitalize;")
        values = JavaStaticMethod("()[Landroid/text/method/TextKeyListener$Capitalize;")
        valueOf = JavaStaticMethod("(Ljava/lang/String;)Landroid/text/method/TextKeyListener$Capitalize;")
        CHARACTERS = JavaStaticField("Landroid/text/method/TextKeyListener$Capitalize;")
        NONE = JavaStaticField("Landroid/text/method/TextKeyListener$Capitalize;")
        SENTENCES = JavaStaticField("Landroid/text/method/TextKeyListener$Capitalize;")
        WORDS = JavaStaticField("Landroid/text/method/TextKeyListener$Capitalize;")