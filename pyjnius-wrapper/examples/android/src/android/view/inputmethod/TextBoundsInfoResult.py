from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["TextBoundsInfoResult"]

class TextBoundsInfoResult(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/view/inputmethod/TextBoundsInfoResult"
    __javaconstructor__ = [("(I)V", False), ("(ILandroid/view/inputmethod/TextBoundsInfo;)V", False)]
    CODE_CANCELLED = JavaStaticField("I")
    CODE_FAILED = JavaStaticField("I")
    CODE_SUCCESS = JavaStaticField("I")
    CODE_UNSUPPORTED = JavaStaticField("I")
    getResultCode = JavaMethod("()I")
    getTextBoundsInfo = JavaMethod("()Landroid/view/inputmethod/TextBoundsInfo;")