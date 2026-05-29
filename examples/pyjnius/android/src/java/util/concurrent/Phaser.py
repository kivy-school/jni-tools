from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Phaser"]

class Phaser(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/concurrent/Phaser"
    __javaconstructor__ = [("()V", False), ("(I)V", False), ("(Ljava/util/concurrent/Phaser;)V", False), ("(Ljava/util/concurrent/Phaser;I)V", False)]
    register = JavaMethod("()I")
    bulkRegister = JavaMethod("(I)I")
    arrive = JavaMethod("()I")
    arriveAndDeregister = JavaMethod("()I")
    arriveAndAwaitAdvance = JavaMethod("()I")
    awaitAdvance = JavaMethod("(I)I")
    awaitAdvanceInterruptibly = JavaMultipleMethod([("(I)I", False, False), ("(IJLjava/util/concurrent/TimeUnit;)I", False, False)])
    forceTermination = JavaMethod("()V")
    getPhase = JavaMethod("()I")
    getRegisteredParties = JavaMethod("()I")
    getArrivedParties = JavaMethod("()I")
    getUnarrivedParties = JavaMethod("()I")
    getParent = JavaMethod("()Ljava/util/concurrent/Phaser;")
    getRoot = JavaMethod("()Ljava/util/concurrent/Phaser;")
    isTerminated = JavaMethod("()Z")
    onAdvance = JavaMethod("(II)Z")
    toString = JavaMethod("()Ljava/lang/String;")