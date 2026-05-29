from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["LoginFilter"]

class LoginFilter(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/text/LoginFilter"
    onInvalidCharacter = JavaMethod("(C)V")
    isAllowed = JavaMethod("(C)Z")
    filter = JavaMethod("(Ljava/lang/CharSequence;IILandroid/text/Spanned;II)Ljava/lang/CharSequence;")
    onStop = JavaMethod("()V")
    onStart = JavaMethod("()V")

    class UsernameFilterGeneric(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/text/LoginFilter$UsernameFilterGeneric"
        __javaconstructor__ = [("(Z)V", False), ("()V", False)]
        isAllowed = JavaMethod("(C)Z")

    class UsernameFilterGMail(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/text/LoginFilter$UsernameFilterGMail"
        __javaconstructor__ = [("(Z)V", False), ("()V", False)]
        isAllowed = JavaMethod("(C)Z")

    class PasswordFilterGMail(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/text/LoginFilter$PasswordFilterGMail"
        __javaconstructor__ = [("(Z)V", False), ("()V", False)]
        isAllowed = JavaMethod("(C)Z")