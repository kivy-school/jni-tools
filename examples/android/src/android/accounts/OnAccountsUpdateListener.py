from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["OnAccountsUpdateListener"]

class OnAccountsUpdateListener(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "android/accounts/OnAccountsUpdateListener"
    onAccountsUpdated = JavaMethod("([Landroid/accounts/Account;)V")