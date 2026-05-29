from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Phaser"]

class Phaser(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/concurrent/Phaser"
    __javaconstructor__ = [("(I)V", False), ("()V", False), ("(Ljava/util/concurrent/Phaser;I)V", False), ("(Ljava/util/concurrent/Phaser;)V", False)]
    toString = JavaMethod("()Ljava/lang/String;")
    register = JavaMethod("()I")
    getParent = JavaMethod("()Ljava/util/concurrent/Phaser;")
    isTerminated = JavaMethod("()Z")
    getRoot = JavaMethod("()Ljava/util/concurrent/Phaser;")
    getPhase = JavaMethod("()I")
    arriveAndAwaitAdvance = JavaMethod("()I")
    bulkRegister = JavaMethod("(I)I")
    arrive = JavaMethod("()I")
    arriveAndDeregister = JavaMethod("()I")
    awaitAdvance = JavaMethod("(I)I")
    awaitAdvanceInterruptibly = JavaMultipleMethod([("(I)I", False, False), ("(IJLjava/util/concurrent/TimeUnit;)I", False, False)])
    forceTermination = JavaMethod("()V")
    getRegisteredParties = JavaMethod("()I")
    getArrivedParties = JavaMethod("()I")
    getUnarrivedParties = JavaMethod("()I")