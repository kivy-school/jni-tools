from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["OptionalLong"]

class OptionalLong(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/OptionalLong"
    empty = JavaStaticMethod("()Ljava/util/OptionalLong;")
    of = JavaStaticMethod("(J)Ljava/util/OptionalLong;")
    getAsLong = JavaMethod("()J")
    isPresent = JavaMethod("()Z")
    isEmpty = JavaMethod("()Z")
    ifPresent = JavaMethod("(Ljava/util/function/LongConsumer;)V")
    ifPresentOrElse = JavaMethod("(Ljava/util/function/LongConsumer;Ljava/lang/Runnable;)V")
    stream = JavaMethod("()Ljava/util/stream/LongStream;")
    orElse = JavaMethod("(J)J")
    orElseGet = JavaMethod("(Ljava/util/function/LongSupplier;)J")
    orElseThrow = JavaMultipleMethod([("()J", False, False), ("(Ljava/util/function/Supplier;)J", False, False)])
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    toString = JavaMethod("()Ljava/lang/String;")