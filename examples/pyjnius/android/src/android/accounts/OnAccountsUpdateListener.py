from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["OnAccountsUpdateListener"]

class OnAccountsUpdateListener(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/accounts/OnAccountsUpdateListener"
    onAccountsUpdated = JavaMethod("([Landroid/accounts/Account;)V")