from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["BaseStream"]

class BaseStream(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/stream/BaseStream"
    iterator = JavaMethod("()Ljava/util/Iterator;")
    spliterator = JavaMethod("()Ljava/util/Spliterator;")
    isParallel = JavaMethod("()Z")
    sequential = JavaMethod("()Ljava/util/stream/BaseStream;")
    parallel = JavaMethod("()Ljava/util/stream/BaseStream;")
    unordered = JavaMethod("()Ljava/util/stream/BaseStream;")
    onClose = JavaMethod("(Ljava/lang/Runnable;)Ljava/util/stream/BaseStream;")
    close = JavaMethod("()V")