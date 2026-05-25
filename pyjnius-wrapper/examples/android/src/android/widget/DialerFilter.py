from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["DialerFilter"]

class DialerFilter(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/widget/DialerFilter"
    __javaconstructor__ = [("(Landroid/content/Context;)V", False), ("(Landroid/content/Context;Landroid/util/AttributeSet;)V", False)]
    DIGITS_AND_LETTERS = JavaStaticField("I")
    DIGITS_AND_LETTERS_NO_DIGITS = JavaStaticField("I")
    DIGITS_AND_LETTERS_NO_LETTERS = JavaStaticField("I")
    DIGITS_ONLY = JavaStaticField("I")
    LETTERS_ONLY = JavaStaticField("I")
    onFinishInflate = JavaMethod("()V")
    onFocusChanged = JavaMethod("(ZILandroid/graphics/Rect;)V")
    isQwertyKeyboard = JavaMethod("()Z")
    onKeyDown = JavaMethod("(ILandroid/view/KeyEvent;)Z")
    onKeyUp = JavaMethod("(ILandroid/view/KeyEvent;)Z")
    getMode = JavaMethod("()I")
    setMode = JavaMethod("(I)V")
    getLetters = JavaMethod("()Ljava/lang/CharSequence;")
    getDigits = JavaMethod("()Ljava/lang/CharSequence;")
    getFilterText = JavaMethod("()Ljava/lang/CharSequence;")
    append = JavaMethod("(Ljava/lang/String;)V")
    clearText = JavaMethod("()V")
    setLettersWatcher = JavaMethod("(Landroid/text/TextWatcher;)V")
    setDigitsWatcher = JavaMethod("(Landroid/text/TextWatcher;)V")
    setFilterWatcher = JavaMethod("(Landroid/text/TextWatcher;)V")
    removeFilterWatcher = JavaMethod("(Landroid/text/TextWatcher;)V")
    onModeChange = JavaMethod("(II)V")