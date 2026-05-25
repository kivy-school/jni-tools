from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["OptionalInt"]

class OptionalInt(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/OptionalInt"
    empty = JavaStaticMethod("()Ljava/util/OptionalInt;")
    of = JavaStaticMethod("(I)Ljava/util/OptionalInt;")
    getAsInt = JavaMethod("()I")
    isPresent = JavaMethod("()Z")
    isEmpty = JavaMethod("()Z")
    ifPresent = JavaMethod("(Ljava/util/function/IntConsumer;)V")
    ifPresentOrElse = JavaMethod("(Ljava/util/function/IntConsumer;Ljava/lang/Runnable;)V")
    stream = JavaMethod("()Ljava/util/stream/IntStream;")
    orElse = JavaMethod("(I)I")
    orElseGet = JavaMethod("(Ljava/util/function/IntSupplier;)I")
    orElseThrow = JavaMultipleMethod([("()I", False, False), ("(Ljava/util/function/Supplier;)I", False, False)])
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    toString = JavaMethod("()Ljava/lang/String;")