from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AccountAuthenticatorActivity"]

class AccountAuthenticatorActivity(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/accounts/AccountAuthenticatorActivity"
    __javaconstructor__ = [("()V", False)]
    setAccountAuthenticatorResult = JavaMethod("(Landroid/os/Bundle;)V")
    onCreate = JavaMethod("(Landroid/os/Bundle;)V")
    finish = JavaMethod("()V")