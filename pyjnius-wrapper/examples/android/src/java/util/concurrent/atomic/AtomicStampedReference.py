from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AtomicStampedReference"]

class AtomicStampedReference(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/concurrent/atomic/AtomicStampedReference"
    __javaconstructor__ = [("(Ljava/lang/Object;I)V", False)]
    getReference = JavaMethod("()Ljava/lang/Object;")
    getStamp = JavaMethod("()I")
    get = JavaMethod("([I)Ljava/lang/Object;")
    weakCompareAndSet = JavaMethod("(Ljava/lang/Object;Ljava/lang/Object;II)Z")
    compareAndSet = JavaMethod("(Ljava/lang/Object;Ljava/lang/Object;II)Z")
    set = JavaMethod("(Ljava/lang/Object;I)V")
    attemptStamp = JavaMethod("(Ljava/lang/Object;I)Z")