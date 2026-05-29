from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["CountedCompleter"]

class CountedCompleter(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/concurrent/CountedCompleter"
    __javaconstructor__ = [("(Ljava/util/concurrent/CountedCompleter;I)V", False), ("(Ljava/util/concurrent/CountedCompleter;)V", False), ("()V", False)]
    compute = JavaMethod("()V")
    onCompletion = JavaMethod("(Ljava/util/concurrent/CountedCompleter;)V")
    onExceptionalCompletion = JavaMethod("(Ljava/lang/Throwable;Ljava/util/concurrent/CountedCompleter;)Z")
    getCompleter = JavaMethod("()Ljava/util/concurrent/CountedCompleter;")
    getPendingCount = JavaMethod("()I")
    setPendingCount = JavaMethod("(I)V")
    addToPendingCount = JavaMethod("(I)V")
    compareAndSetPendingCount = JavaMethod("(II)Z")
    decrementPendingCountUnlessZero = JavaMethod("()I")
    getRoot = JavaMethod("()Ljava/util/concurrent/CountedCompleter;")
    tryComplete = JavaMethod("()V")
    propagateCompletion = JavaMethod("()V")
    complete = JavaMethod("(Ljava/lang/Object;)V")
    firstComplete = JavaMethod("()Ljava/util/concurrent/CountedCompleter;")
    nextComplete = JavaMethod("()Ljava/util/concurrent/CountedCompleter;")
    quietlyCompleteRoot = JavaMethod("()V")
    helpComplete = JavaMethod("(I)V")
    exec = JavaMethod("()Z")
    getRawResult = JavaMethod("()Ljava/lang/Object;")
    setRawResult = JavaMethod("(Ljava/lang/Object;)V")