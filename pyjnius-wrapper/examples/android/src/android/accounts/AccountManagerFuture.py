from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AccountManagerFuture"]

class AccountManagerFuture(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "android/accounts/AccountManagerFuture"
    cancel = JavaMethod("(Z)Z")
    isCancelled = JavaMethod("()Z")
    isDone = JavaMethod("()Z")
    getResult = JavaMultipleMethod([("()Ljava/lang/Object;", False, False), ("(JLjava/util/concurrent/TimeUnit;)Ljava/lang/Object;", False, False)])