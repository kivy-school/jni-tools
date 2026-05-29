from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["CyclicBarrier"]

class CyclicBarrier(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/concurrent/CyclicBarrier"
    __javaconstructor__ = [("(ILjava/lang/Runnable;)V", False), ("(I)V", False)]
    getParties = JavaMethod("()I")
    await = JavaMultipleMethod([("()I", False, False), ("(JLjava/util/concurrent/TimeUnit;)I", False, False)])
    isBroken = JavaMethod("()Z")
    reset = JavaMethod("()V")
    getNumberWaiting = JavaMethod("()I")