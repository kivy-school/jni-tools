from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["PrintJob"]

class PrintJob(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/print/PrintJob"
    getId = JavaMethod("()Landroid/print/PrintJobId;")
    getInfo = JavaMethod("()Landroid/print/PrintJobInfo;")
    cancel = JavaMethod("()V")
    restart = JavaMethod("()V")
    isQueued = JavaMethod("()Z")
    isStarted = JavaMethod("()Z")
    isBlocked = JavaMethod("()Z")
    isCompleted = JavaMethod("()Z")
    isFailed = JavaMethod("()Z")
    isCancelled = JavaMethod("()Z")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")