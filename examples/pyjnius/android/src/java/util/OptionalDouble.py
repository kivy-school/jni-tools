from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["OptionalDouble"]

class OptionalDouble(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/OptionalDouble"
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    of = JavaStaticMethod("(D)Ljava/util/OptionalDouble;")
    isEmpty = JavaMethod("()Z")
    stream = JavaMethod("()Ljava/util/stream/DoubleStream;")
    empty = JavaStaticMethod("()Ljava/util/OptionalDouble;")
    orElse = JavaMethod("(D)D")
    isPresent = JavaMethod("()Z")
    orElseThrow = JavaMultipleMethod([("(Ljava/util/function/Supplier;)D", False, False), ("()D", False, False)])
    getAsDouble = JavaMethod("()D")
    ifPresent = JavaMethod("(Ljava/util/function/DoubleConsumer;)V")
    ifPresentOrElse = JavaMethod("(Ljava/util/function/DoubleConsumer;Ljava/lang/Runnable;)V")
    orElseGet = JavaMethod("(Ljava/util/function/DoubleSupplier;)D")