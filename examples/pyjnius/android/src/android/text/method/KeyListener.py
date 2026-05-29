from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["KeyListener"]

class KeyListener(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/text/method/KeyListener"
    onKeyDown = JavaMethod("(Landroid/view/View;Landroid/text/Editable;ILandroid/view/KeyEvent;)Z")
    onKeyUp = JavaMethod("(Landroid/view/View;Landroid/text/Editable;ILandroid/view/KeyEvent;)Z")
    getInputType = JavaMethod("()I")
    onKeyOther = JavaMethod("(Landroid/view/View;Landroid/text/Editable;Landroid/view/KeyEvent;)Z")
    clearMetaKeyState = JavaMethod("(Landroid/view/View;Landroid/text/Editable;I)V")