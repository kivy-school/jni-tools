from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AccountManagerCallback"]

class AccountManagerCallback(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "android/accounts/AccountManagerCallback"
    run = JavaMethod("(Landroid/accounts/AccountManagerFuture;)V")