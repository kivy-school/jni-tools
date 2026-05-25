from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["PhoneNumberFormattingTextWatcher"]

class PhoneNumberFormattingTextWatcher(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/telephony/PhoneNumberFormattingTextWatcher"
    __javaconstructor__ = [("()V", False), ("(Ljava/lang/String;)V", False)]
    beforeTextChanged = JavaMethod("(Ljava/lang/CharSequence;III)V")
    onTextChanged = JavaMethod("(Ljava/lang/CharSequence;III)V")
    afterTextChanged = JavaMethod("(Landroid/text/Editable;)V")