from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["MultiAutoCompleteTextView"]

class MultiAutoCompleteTextView(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/widget/MultiAutoCompleteTextView"
    __javaconstructor__ = [("(Landroid/content/Context;)V", False), ("(Landroid/content/Context;Landroid/util/AttributeSet;)V", False), ("(Landroid/content/Context;Landroid/util/AttributeSet;I)V", False), ("(Landroid/content/Context;Landroid/util/AttributeSet;II)V", False)]
    setTokenizer = JavaMethod("(Landroid/widget/MultiAutoCompleteTextView$Tokenizer;)V")
    performFiltering = JavaMultipleMethod([("(Ljava/lang/CharSequence;I)V", False, False), ("(Ljava/lang/CharSequence;III)V", False, False)])
    enoughToFilter = JavaMethod("()Z")
    performValidation = JavaMethod("()V")
    replaceText = JavaMethod("(Ljava/lang/CharSequence;)V")
    getAccessibilityClassName = JavaMethod("()Ljava/lang/CharSequence;")

    class CommaTokenizer(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/widget/MultiAutoCompleteTextView/CommaTokenizer"
        __javaconstructor__ = [("()V", False)]
        findTokenStart = JavaMethod("(Ljava/lang/CharSequence;I)I")
        findTokenEnd = JavaMethod("(Ljava/lang/CharSequence;I)I")
        terminateToken = JavaMethod("(Ljava/lang/CharSequence;)Ljava/lang/CharSequence;")

    class Tokenizer(JavaInterface, metaclass=MetaJavaClass):
        __javaclass__ = "android/widget/MultiAutoCompleteTextView/Tokenizer"
        findTokenStart = JavaMethod("(Ljava/lang/CharSequence;I)I")
        findTokenEnd = JavaMethod("(Ljava/lang/CharSequence;I)I")
        terminateToken = JavaMethod("(Ljava/lang/CharSequence;)Ljava/lang/CharSequence;")