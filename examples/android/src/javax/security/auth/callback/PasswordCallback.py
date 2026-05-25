from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["PasswordCallback"]

class PasswordCallback(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/security/auth/callback/PasswordCallback"
    __javaconstructor__ = [("(Ljava/lang/String;Z)V", False)]
    getPrompt = JavaMethod("()Ljava/lang/String;")
    isEchoOn = JavaMethod("()Z")
    setPassword = JavaMethod("([C)V")
    getPassword = JavaMethod("()[C")
    clearPassword = JavaMethod("()V")