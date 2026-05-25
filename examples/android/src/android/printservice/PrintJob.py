from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["PrintJob"]

class PrintJob(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/printservice/PrintJob"
    getId = JavaMethod("()Landroid/print/PrintJobId;")
    getInfo = JavaMethod("()Landroid/print/PrintJobInfo;")
    getDocument = JavaMethod("()Landroid/printservice/PrintDocument;")
    isQueued = JavaMethod("()Z")
    isStarted = JavaMethod("()Z")
    isBlocked = JavaMethod("()Z")
    isCompleted = JavaMethod("()Z")
    isFailed = JavaMethod("()Z")
    isCancelled = JavaMethod("()Z")
    start = JavaMethod("()Z")
    block = JavaMethod("(Ljava/lang/String;)Z")
    complete = JavaMethod("()Z")
    fail = JavaMethod("(Ljava/lang/String;)Z")
    cancel = JavaMethod("()Z")
    setProgress = JavaMethod("(F)V")
    setStatus = JavaMultipleMethod([("(Ljava/lang/CharSequence;)V", False, False), ("(I)V", False, False)])
    setTag = JavaMethod("(Ljava/lang/String;)Z")
    getTag = JavaMethod("()Ljava/lang/String;")
    getAdvancedStringOption = JavaMethod("(Ljava/lang/String;)Ljava/lang/String;")
    hasAdvancedOption = JavaMethod("(Ljava/lang/String;)Z")
    getAdvancedIntOption = JavaMethod("(Ljava/lang/String;)I")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")