from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["TextKeyListener"]

class TextKeyListener(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/text/method/TextKeyListener"
    __javaconstructor__ = [("(Landroid/text/method/TextKeyListener$Capitalize;Z)V", False)]
    getInstance = JavaMultipleMethod([("(ZLandroid/text/method/TextKeyListener$Capitalize;)Landroid/text/method/TextKeyListener;", True, False), ("()Landroid/text/method/TextKeyListener;", True, False)])
    shouldCap = JavaStaticMethod("(Landroid/text/method/TextKeyListener$Capitalize;Ljava/lang/CharSequence;I)Z")
    getInputType = JavaMethod("()I")
    onKeyDown = JavaMethod("(Landroid/view/View;Landroid/text/Editable;ILandroid/view/KeyEvent;)Z")
    onKeyUp = JavaMethod("(Landroid/view/View;Landroid/text/Editable;ILandroid/view/KeyEvent;)Z")
    onKeyOther = JavaMethod("(Landroid/view/View;Landroid/text/Editable;Landroid/view/KeyEvent;)Z")
    clear = JavaStaticMethod("(Landroid/text/Editable;)V")
    onSpanAdded = JavaMethod("(Landroid/text/Spannable;Ljava/lang/Object;II)V")
    onSpanRemoved = JavaMethod("(Landroid/text/Spannable;Ljava/lang/Object;II)V")
    onSpanChanged = JavaMethod("(Landroid/text/Spannable;Ljava/lang/Object;IIII)V")
    release = JavaMethod("()V")

    class Capitalize(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/text/method/TextKeyListener/Capitalize"
        values = JavaStaticMethod("()[Landroid/text/method/TextKeyListener$Capitalize;")
        valueOf = JavaStaticMethod("(Ljava/lang/String;)Landroid/text/method/TextKeyListener$Capitalize;")
        NONE = JavaStaticField("Landroid/text/method/TextKeyListener/Capitalize;")
        SENTENCES = JavaStaticField("Landroid/text/method/TextKeyListener/Capitalize;")
        WORDS = JavaStaticField("Landroid/text/method/TextKeyListener/Capitalize;")
        CHARACTERS = JavaStaticField("Landroid/text/method/TextKeyListener/Capitalize;")