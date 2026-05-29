from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["PasswordTransformationMethod"]

class PasswordTransformationMethod(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/text/method/PasswordTransformationMethod"
    __javaconstructor__ = [("()V", False)]
    getTransformation = JavaMethod("(Ljava/lang/CharSequence;Landroid/view/View;)Ljava/lang/CharSequence;")
    getInstance = JavaStaticMethod("()Landroid/text/method/PasswordTransformationMethod;")
    beforeTextChanged = JavaMethod("(Ljava/lang/CharSequence;III)V")
    onTextChanged = JavaMethod("(Ljava/lang/CharSequence;III)V")
    afterTextChanged = JavaMethod("(Landroid/text/Editable;)V")
    onFocusChanged = JavaMethod("(Landroid/view/View;Ljava/lang/CharSequence;ZILandroid/graphics/Rect;)V")