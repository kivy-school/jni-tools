from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AtomicBoolean"]

class AtomicBoolean(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/concurrent/atomic/AtomicBoolean"
    __javaconstructor__ = [("(Z)V", False), ("()V", False)]
    get = JavaMethod("()Z")
    compareAndSet = JavaMethod("(ZZ)Z")
    weakCompareAndSet = JavaMethod("(ZZ)Z")
    weakCompareAndSetPlain = JavaMethod("(ZZ)Z")
    set = JavaMethod("(Z)V")
    lazySet = JavaMethod("(Z)V")
    getAndSet = JavaMethod("(Z)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    getPlain = JavaMethod("()Z")
    setPlain = JavaMethod("(Z)V")
    getOpaque = JavaMethod("()Z")
    setOpaque = JavaMethod("(Z)V")
    getAcquire = JavaMethod("()Z")
    setRelease = JavaMethod("(Z)V")
    compareAndExchange = JavaMethod("(ZZ)Z")
    compareAndExchangeAcquire = JavaMethod("(ZZ)Z")
    compareAndExchangeRelease = JavaMethod("(ZZ)Z")
    weakCompareAndSetVolatile = JavaMethod("(ZZ)Z")
    weakCompareAndSetAcquire = JavaMethod("(ZZ)Z")
    weakCompareAndSetRelease = JavaMethod("(ZZ)Z")