from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["OptionalInt"]

class OptionalInt(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/OptionalInt"
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    of = JavaStaticMethod("(I)Ljava/util/OptionalInt;")
    isEmpty = JavaMethod("()Z")
    stream = JavaMethod("()Ljava/util/stream/IntStream;")
    empty = JavaStaticMethod("()Ljava/util/OptionalInt;")
    orElse = JavaMethod("(I)I")
    isPresent = JavaMethod("()Z")
    orElseThrow = JavaMultipleMethod([("(Ljava/util/function/Supplier;)I", False, False), ("()I", False, False)])
    getAsInt = JavaMethod("()I")
    ifPresent = JavaMethod("(Ljava/util/function/IntConsumer;)V")
    ifPresentOrElse = JavaMethod("(Ljava/util/function/IntConsumer;Ljava/lang/Runnable;)V")
    orElseGet = JavaMethod("(Ljava/util/function/IntSupplier;)I")