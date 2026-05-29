from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["CyclicBarrier"]

class CyclicBarrier(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/concurrent/CyclicBarrier"
    __javaconstructor__ = [("(I)V", False), ("(ILjava/lang/Runnable;)V", False)]
    reset = JavaMethod("()V")
    await = JavaMultipleMethod([("()I", False, False), ("(JLjava/util/concurrent/TimeUnit;)I", False, False)])
    getParties = JavaMethod("()I")
    isBroken = JavaMethod("()Z")
    getNumberWaiting = JavaMethod("()I")