from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AtomicMarkableReference"]

class AtomicMarkableReference(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/concurrent/atomic/AtomicMarkableReference"
    __javaconstructor__ = [("(Ljava/lang/Object;Z)V", False)]
    getReference = JavaMethod("()Ljava/lang/Object;")
    isMarked = JavaMethod("()Z")
    get = JavaMethod("([Z)Ljava/lang/Object;")
    weakCompareAndSet = JavaMethod("(Ljava/lang/Object;Ljava/lang/Object;ZZ)Z")
    compareAndSet = JavaMethod("(Ljava/lang/Object;Ljava/lang/Object;ZZ)Z")
    set = JavaMethod("(Ljava/lang/Object;Z)V")
    attemptMark = JavaMethod("(Ljava/lang/Object;Z)Z")