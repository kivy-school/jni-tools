from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["KeyListener"]

class KeyListener(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "android/text/method/KeyListener"
    getInputType = JavaMethod("()I")
    onKeyDown = JavaMethod("(Landroid/view/View;Landroid/text/Editable;ILandroid/view/KeyEvent;)Z")
    onKeyUp = JavaMethod("(Landroid/view/View;Landroid/text/Editable;ILandroid/view/KeyEvent;)Z")
    onKeyOther = JavaMethod("(Landroid/view/View;Landroid/text/Editable;Landroid/view/KeyEvent;)Z")
    clearMetaKeyState = JavaMethod("(Landroid/view/View;Landroid/text/Editable;I)V")