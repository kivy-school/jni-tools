from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AtomicMarkableReference"]

class AtomicMarkableReference(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/concurrent/atomic/AtomicMarkableReference"
    __javaconstructor__ = [("(Ljava/lang/Object;Z)V", False)]
    getReference = JavaMethod("()Ljava/lang/Object;")
    get = JavaMethod("([Z)Ljava/lang/Object;")
    set = JavaMethod("(Ljava/lang/Object;Z)V")
    compareAndSet = JavaMethod("(Ljava/lang/Object;Ljava/lang/Object;ZZ)Z")
    weakCompareAndSet = JavaMethod("(Ljava/lang/Object;Ljava/lang/Object;ZZ)Z")
    isMarked = JavaMethod("()Z")
    attemptMark = JavaMethod("(Ljava/lang/Object;Z)Z")