from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["BaseKeyListener"]

class BaseKeyListener(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/text/method/BaseKeyListener"
    __javaconstructor__ = [("()V", False)]
    backspace = JavaMethod("(Landroid/view/View;Landroid/text/Editable;ILandroid/view/KeyEvent;)Z")
    forwardDelete = JavaMethod("(Landroid/view/View;Landroid/text/Editable;ILandroid/view/KeyEvent;)Z")
    onKeyDown = JavaMethod("(Landroid/view/View;Landroid/text/Editable;ILandroid/view/KeyEvent;)Z")
    onKeyOther = JavaMethod("(Landroid/view/View;Landroid/text/Editable;Landroid/view/KeyEvent;)Z")