from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["PasswordTransformationMethod"]

class PasswordTransformationMethod(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/text/method/PasswordTransformationMethod"
    __javaconstructor__ = [("()V", False)]
    getInstance = JavaStaticMethod("()Landroid/text/method/PasswordTransformationMethod;")
    onFocusChanged = JavaMethod("(Landroid/view/View;Ljava/lang/CharSequence;ZILandroid/graphics/Rect;)V")
    getTransformation = JavaMethod("(Ljava/lang/CharSequence;Landroid/view/View;)Ljava/lang/CharSequence;")
    afterTextChanged = JavaMethod("(Landroid/text/Editable;)V")
    beforeTextChanged = JavaMethod("(Ljava/lang/CharSequence;III)V")
    onTextChanged = JavaMethod("(Ljava/lang/CharSequence;III)V")