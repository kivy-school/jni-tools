from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["PrintJob"]

class PrintJob(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/print/PrintJob"
    isBlocked = JavaMethod("()Z")
    getInfo = JavaMethod("()Landroid/print/PrintJobInfo;")
    isFailed = JavaMethod("()Z")
    isCompleted = JavaMethod("()Z")
    isCancelled = JavaMethod("()Z")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    getId = JavaMethod("()Landroid/print/PrintJobId;")
    cancel = JavaMethod("()V")
    isStarted = JavaMethod("()Z")
    isQueued = JavaMethod("()Z")
    restart = JavaMethod("()V")