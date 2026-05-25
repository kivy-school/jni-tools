from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["TextSnapshot"]

class TextSnapshot(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/view/inputmethod/TextSnapshot"
    __javaconstructor__ = [("(Landroid/view/inputmethod/SurroundingText;III)V", False)]
    getSurroundingText = JavaMethod("()Landroid/view/inputmethod/SurroundingText;")
    getSelectionStart = JavaMethod("()I")
    getSelectionEnd = JavaMethod("()I")
    getCompositionStart = JavaMethod("()I")
    getCompositionEnd = JavaMethod("()I")
    getCursorCapsMode = JavaMethod("()I")