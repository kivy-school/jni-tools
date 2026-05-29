from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AccountManagerCallback"]

class AccountManagerCallback(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/accounts/AccountManagerCallback"
    run = JavaMethod("(Landroid/accounts/AccountManagerFuture;)V")