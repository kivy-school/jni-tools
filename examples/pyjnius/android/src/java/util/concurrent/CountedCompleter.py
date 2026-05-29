from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["CountedCompleter"]

class CountedCompleter(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/concurrent/CountedCompleter"
    compute = JavaMethod("()V")
    getRoot = JavaMethod("()Ljava/util/concurrent/CountedCompleter;")
    onCompletion = JavaMethod("(Ljava/util/concurrent/CountedCompleter;)V")
    tryComplete = JavaMethod("()V")
    firstComplete = JavaMethod("()Ljava/util/concurrent/CountedCompleter;")
    helpComplete = JavaMethod("(I)V")
    onExceptionalCompletion = JavaMethod("(Ljava/lang/Throwable;Ljava/util/concurrent/CountedCompleter;)Z")
    getCompleter = JavaMethod("()Ljava/util/concurrent/CountedCompleter;")
    getPendingCount = JavaMethod("()I")
    setPendingCount = JavaMethod("(I)V")
    addToPendingCount = JavaMethod("(I)V")
    compareAndSetPendingCount = JavaMethod("(II)Z")
    decrementPendingCountUnlessZero = JavaMethod("()I")
    propagateCompletion = JavaMethod("()V")
    nextComplete = JavaMethod("()Ljava/util/concurrent/CountedCompleter;")
    quietlyCompleteRoot = JavaMethod("()V")
    getRawResult = JavaMethod("()Ljava/lang/Object;")
    complete = JavaMethod("(Ljava/lang/Object;)V")