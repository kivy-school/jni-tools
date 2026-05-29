from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["TextSnapshot"]

class TextSnapshot(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/view/inputmethod/TextSnapshot"
    __javaconstructor__ = [("(Landroid/view/inputmethod/SurroundingText;III)V", False)]
    getCompositionEnd = JavaMethod("()I")
    getCompositionStart = JavaMethod("()I")
    getSelectionEnd = JavaMethod("()I")
    getSelectionStart = JavaMethod("()I")
    getCursorCapsMode = JavaMethod("()I")
    getSurroundingText = JavaMethod("()Landroid/view/inputmethod/SurroundingText;")