from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AccountManagerFuture"]

class AccountManagerFuture(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/accounts/AccountManagerFuture"
    isCancelled = JavaMethod("()Z")
    isDone = JavaMethod("()Z")
    cancel = JavaMethod("(Z)Z")
    getResult = JavaMultipleMethod([("()Ljava/lang/Object;", False, False), ("(JLjava/util/concurrent/TimeUnit;)Ljava/lang/Object;", False, False)])