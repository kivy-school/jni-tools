from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["TextWatcher"]

class TextWatcher(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/text/TextWatcher"
    afterTextChanged = JavaMethod("(Landroid/text/Editable;)V")
    beforeTextChanged = JavaMethod("(Ljava/lang/CharSequence;III)V")
    onTextChanged = JavaMethod("(Ljava/lang/CharSequence;III)V")