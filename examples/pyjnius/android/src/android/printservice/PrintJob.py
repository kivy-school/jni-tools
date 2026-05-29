from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["PrintJob"]

class PrintJob(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/printservice/PrintJob"
    isBlocked = JavaMethod("()Z")
    getInfo = JavaMethod("()Landroid/print/PrintJobInfo;")
    getDocument = JavaMethod("()Landroid/printservice/PrintDocument;")
    getAdvancedIntOption = JavaMethod("(Ljava/lang/String;)I")
    getAdvancedStringOption = JavaMethod("(Ljava/lang/String;)Ljava/lang/String;")
    hasAdvancedOption = JavaMethod("(Ljava/lang/String;)Z")
    isFailed = JavaMethod("()Z")
    isCompleted = JavaMethod("()Z")
    setStatus = JavaMultipleMethod([("(Ljava/lang/CharSequence;)V", False, False), ("(I)V", False, False)])
    isCancelled = JavaMethod("()Z")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    start = JavaMethod("()Z")
    getId = JavaMethod("()Landroid/print/PrintJobId;")
    cancel = JavaMethod("()Z")
    isStarted = JavaMethod("()Z")
    fail = JavaMethod("(Ljava/lang/String;)Z")
    getTag = JavaMethod("()Ljava/lang/String;")
    setTag = JavaMethod("(Ljava/lang/String;)Z")
    isQueued = JavaMethod("()Z")
    setProgress = JavaMethod("(F)V")
    block = JavaMethod("(Ljava/lang/String;)Z")
    complete = JavaMethod("()Z")