from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["OptionalDouble"]

class OptionalDouble(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/OptionalDouble"
    empty = JavaStaticMethod("()Ljava/util/OptionalDouble;")
    of = JavaStaticMethod("(D)Ljava/util/OptionalDouble;")
    getAsDouble = JavaMethod("()D")
    isPresent = JavaMethod("()Z")
    isEmpty = JavaMethod("()Z")
    ifPresent = JavaMethod("(Ljava/util/function/DoubleConsumer;)V")
    ifPresentOrElse = JavaMethod("(Ljava/util/function/DoubleConsumer;Ljava/lang/Runnable;)V")
    stream = JavaMethod("()Ljava/util/stream/DoubleStream;")
    orElse = JavaMethod("(D)D")
    orElseGet = JavaMethod("(Ljava/util/function/DoubleSupplier;)D")
    orElseThrow = JavaMultipleMethod([("()D", False, False), ("(Ljava/util/function/Supplier;)D", False, False)])
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    toString = JavaMethod("()Ljava/lang/String;")