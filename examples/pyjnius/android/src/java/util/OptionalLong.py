from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["OptionalLong"]

class OptionalLong(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/OptionalLong"
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    of = JavaStaticMethod("(J)Ljava/util/OptionalLong;")
    isEmpty = JavaMethod("()Z")
    stream = JavaMethod("()Ljava/util/stream/LongStream;")
    empty = JavaStaticMethod("()Ljava/util/OptionalLong;")
    orElse = JavaMethod("(J)J")
    isPresent = JavaMethod("()Z")
    orElseThrow = JavaMultipleMethod([("(Ljava/util/function/Supplier;)J", False, False), ("()J", False, False)])
    getAsLong = JavaMethod("()J")
    ifPresent = JavaMethod("(Ljava/util/function/LongConsumer;)V")
    ifPresentOrElse = JavaMethod("(Ljava/util/function/LongConsumer;Ljava/lang/Runnable;)V")
    orElseGet = JavaMethod("(Ljava/util/function/LongSupplier;)J")