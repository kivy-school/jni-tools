from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Collector"]

class Collector(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/stream/Collector"
    of = JavaMultipleMethod([("(Ljava/util/function/Supplier;Ljava/util/function/BiConsumer;Ljava/util/function/BinaryOperator;[Ljava/util/stream/Collector$Characteristics;)Ljava/util/stream/Collector;", True, True), ("(Ljava/util/function/Supplier;Ljava/util/function/BiConsumer;Ljava/util/function/BinaryOperator;Ljava/util/function/Function;[Ljava/util/stream/Collector$Characteristics;)Ljava/util/stream/Collector;", True, True)])
    characteristics = JavaMethod("()Ljava/util/Set;")
    accumulator = JavaMethod("()Ljava/util/function/BiConsumer;")
    finisher = JavaMethod("()Ljava/util/function/Function;")
    combiner = JavaMethod("()Ljava/util/function/BinaryOperator;")
    supplier = JavaMethod("()Ljava/util/function/Supplier;")

    class Characteristics(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "java/util/stream/Collector$Characteristics"
        CONCURRENT = JavaStaticField("Ljava/util/stream/Collector$Characteristics;")
        UNORDERED = JavaStaticField("Ljava/util/stream/Collector$Characteristics;")
        IDENTITY_FINISH = JavaStaticField("Ljava/util/stream/Collector$Characteristics;")
        values = JavaStaticMethod("()[Ljava/util/stream/Collector$Characteristics;")
        valueOf = JavaStaticMethod("(Ljava/lang/String;)Ljava/util/stream/Collector$Characteristics;")
        CONCURRENT = JavaStaticField("Ljava/util/stream/Collector$Characteristics;")
        UNORDERED = JavaStaticField("Ljava/util/stream/Collector$Characteristics;")
        IDENTITY_FINISH = JavaStaticField("Ljava/util/stream/Collector$Characteristics;")