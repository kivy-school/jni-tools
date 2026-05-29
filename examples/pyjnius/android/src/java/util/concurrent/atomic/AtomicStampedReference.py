from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AtomicStampedReference"]

class AtomicStampedReference(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/concurrent/atomic/AtomicStampedReference"
    __javaconstructor__ = [("(Ljava/lang/Object;I)V", False)]
    getStamp = JavaMethod("()I")
    getReference = JavaMethod("()Ljava/lang/Object;")
    get = JavaMethod("([I)Ljava/lang/Object;")
    set = JavaMethod("(Ljava/lang/Object;I)V")
    compareAndSet = JavaMethod("(Ljava/lang/Object;Ljava/lang/Object;II)Z")
    weakCompareAndSet = JavaMethod("(Ljava/lang/Object;Ljava/lang/Object;II)Z")
    attemptStamp = JavaMethod("(Ljava/lang/Object;I)Z")