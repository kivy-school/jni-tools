from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["QwertyKeyListener"]

class QwertyKeyListener(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/text/method/QwertyKeyListener"
    __javaconstructor__ = [("(Landroid/text/method/TextKeyListener$Capitalize;Z)V", False)]
    getInstance = JavaStaticMethod("(ZLandroid/text/method/TextKeyListener$Capitalize;)Landroid/text/method/QwertyKeyListener;")
    getInstanceForFullKeyboard = JavaStaticMethod("()Landroid/text/method/QwertyKeyListener;")
    getInputType = JavaMethod("()I")
    onKeyDown = JavaMethod("(Landroid/view/View;Landroid/text/Editable;ILandroid/view/KeyEvent;)Z")
    markAsReplaced = JavaStaticMethod("(Landroid/text/Spannable;IILjava/lang/String;)V")