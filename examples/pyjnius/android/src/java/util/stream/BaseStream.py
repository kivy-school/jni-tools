from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["BaseStream"]

class BaseStream(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/stream/BaseStream"
    iterator = JavaMethod("()Ljava/util/Iterator;")
    spliterator = JavaMethod("()Ljava/util/Spliterator;")
    close = JavaMethod("()V")
    parallel = JavaMethod("()Ljava/util/stream/BaseStream;")
    isParallel = JavaMethod("()Z")
    sequential = JavaMethod("()Ljava/util/stream/BaseStream;")
    unordered = JavaMethod("()Ljava/util/stream/BaseStream;")
    onClose = JavaMethod("(Ljava/lang/Runnable;)Ljava/util/stream/BaseStream;")