from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AtomicBoolean"]

class AtomicBoolean(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/concurrent/atomic/AtomicBoolean"
    __javaconstructor__ = [("(Z)V", False), ("()V", False)]
    toString = JavaMethod("()Ljava/lang/String;")
    get = JavaMethod("()Z")
    set = JavaMethod("(Z)V")
    getOpaque = JavaMethod("()Z")
    setOpaque = JavaMethod("(Z)V")
    getAcquire = JavaMethod("()Z")
    setRelease = JavaMethod("(Z)V")
    compareAndSet = JavaMethod("(ZZ)Z")
    compareAndExchange = JavaMethod("(ZZ)Z")
    compareAndExchangeAcquire = JavaMethod("(ZZ)Z")
    compareAndExchangeRelease = JavaMethod("(ZZ)Z")
    weakCompareAndSetPlain = JavaMethod("(ZZ)Z")
    weakCompareAndSet = JavaMethod("(ZZ)Z")
    weakCompareAndSetAcquire = JavaMethod("(ZZ)Z")
    weakCompareAndSetRelease = JavaMethod("(ZZ)Z")
    getAndSet = JavaMethod("(Z)Z")
    weakCompareAndSetVolatile = JavaMethod("(ZZ)Z")
    lazySet = JavaMethod("(Z)V")
    getPlain = JavaMethod("()Z")
    setPlain = JavaMethod("(Z)V")