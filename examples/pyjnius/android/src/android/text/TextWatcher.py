from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["TextWatcher"]

class TextWatcher(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "android/text/TextWatcher"
    beforeTextChanged = JavaMethod("(Ljava/lang/CharSequence;III)V")
    onTextChanged = JavaMethod("(Ljava/lang/CharSequence;III)V")
    afterTextChanged = JavaMethod("(Landroid/text/Editable;)V")