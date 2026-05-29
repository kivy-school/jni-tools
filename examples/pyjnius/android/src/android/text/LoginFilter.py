from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["LoginFilter"]

class LoginFilter(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/text/LoginFilter"
    filter = JavaMethod("(Ljava/lang/CharSequence;IILandroid/text/Spanned;II)Ljava/lang/CharSequence;")
    onStart = JavaMethod("()V")
    onInvalidCharacter = JavaMethod("(C)V")
    onStop = JavaMethod("()V")
    isAllowed = JavaMethod("(C)Z")

    class PasswordFilterGMail(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/text/LoginFilter/PasswordFilterGMail"
        __javaconstructor__ = [("()V", False), ("(Z)V", False)]
        isAllowed = JavaMethod("(C)Z")

    class UsernameFilterGMail(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/text/LoginFilter/UsernameFilterGMail"
        __javaconstructor__ = [("()V", False), ("(Z)V", False)]
        isAllowed = JavaMethod("(C)Z")

    class UsernameFilterGeneric(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/text/LoginFilter/UsernameFilterGeneric"
        __javaconstructor__ = [("()V", False), ("(Z)V", False)]
        isAllowed = JavaMethod("(C)Z")