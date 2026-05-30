from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

class LongFunction(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/function/LongFunction"
    apply = JavaMethod("(J)Ljava/lang/Object;")

class IntConsumer(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/function/IntConsumer"
    accept = JavaMethod("(I)V")
    andThen = JavaMethod("(Ljava/util/function/IntConsumer;)Ljava/util/function/IntConsumer;")

class IntFunction(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/function/IntFunction"
    apply = JavaMethod("(I)Ljava/lang/Object;")

class ObjIntConsumer(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/function/ObjIntConsumer"
    accept = JavaMethod("(Ljava/lang/Object;I)V")

class BinaryOperator(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/function/BinaryOperator"
    minBy = JavaStaticMethod("(Ljava/util/Comparator;)Ljava/util/function/BinaryOperator;")
    maxBy = JavaStaticMethod("(Ljava/util/Comparator;)Ljava/util/function/BinaryOperator;")

class UnaryOperator(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/function/UnaryOperator"
    identity = JavaStaticMethod("()Ljava/util/function/UnaryOperator;")

class LongSupplier(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/function/LongSupplier"
    getAsLong = JavaMethod("()J")

class LongToDoubleFunction(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/function/LongToDoubleFunction"
    applyAsDouble = JavaMethod("(J)D")

class IntToDoubleFunction(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/function/IntToDoubleFunction"
    applyAsDouble = JavaMethod("(I)D")

class BiPredicate(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/function/BiPredicate"
    test = JavaMethod("(Ljava/lang/Object;Ljava/lang/Object;)Z")
    negate = JavaMethod("()Ljava/util/function/BiPredicate;")
    and = JavaMethod("(Ljava/util/function/BiPredicate;)Ljava/util/function/BiPredicate;")
    or = JavaMethod("(Ljava/util/function/BiPredicate;)Ljava/util/function/BiPredicate;")

class LongBinaryOperator(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/function/LongBinaryOperator"
    applyAsLong = JavaMethod("(JJ)J")

class IntBinaryOperator(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/function/IntBinaryOperator"
    applyAsInt = JavaMethod("(II)I")

class ToDoubleBiFunction(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/function/ToDoubleBiFunction"
    applyAsDouble = JavaMethod("(Ljava/lang/Object;Ljava/lang/Object;)D")

class DoubleBinaryOperator(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/function/DoubleBinaryOperator"
    applyAsDouble = JavaMethod("(DD)D")

class LongUnaryOperator(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/function/LongUnaryOperator"
    identity = JavaStaticMethod("()Ljava/util/function/LongUnaryOperator;")
    applyAsLong = JavaMethod("(J)J")
    compose = JavaMethod("(Ljava/util/function/LongUnaryOperator;)Ljava/util/function/LongUnaryOperator;")
    andThen = JavaMethod("(Ljava/util/function/LongUnaryOperator;)Ljava/util/function/LongUnaryOperator;")

class DoubleUnaryOperator(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/function/DoubleUnaryOperator"
    identity = JavaStaticMethod("()Ljava/util/function/DoubleUnaryOperator;")
    applyAsDouble = JavaMethod("(D)D")
    compose = JavaMethod("(Ljava/util/function/DoubleUnaryOperator;)Ljava/util/function/DoubleUnaryOperator;")
    andThen = JavaMethod("(Ljava/util/function/DoubleUnaryOperator;)Ljava/util/function/DoubleUnaryOperator;")

class ToIntBiFunction(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/function/ToIntBiFunction"
    applyAsInt = JavaMethod("(Ljava/lang/Object;Ljava/lang/Object;)I")

class ToIntFunction(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/function/ToIntFunction"
    applyAsInt = JavaMethod("(Ljava/lang/Object;)I")

class DoublePredicate(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/function/DoublePredicate"
    test = JavaMethod("(D)Z")
    negate = JavaMethod("()Ljava/util/function/DoublePredicate;")
    and = JavaMethod("(Ljava/util/function/DoublePredicate;)Ljava/util/function/DoublePredicate;")
    or = JavaMethod("(Ljava/util/function/DoublePredicate;)Ljava/util/function/DoublePredicate;")

class DoubleSupplier(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/function/DoubleSupplier"
    getAsDouble = JavaMethod("()D")

class ObjDoubleConsumer(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/function/ObjDoubleConsumer"
    accept = JavaMethod("(Ljava/lang/Object;D)V")

class Supplier(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/function/Supplier"
    get = JavaMethod("()Ljava/lang/Object;")

class BiFunction(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/function/BiFunction"
    apply = JavaMethod("(Ljava/lang/Object;Ljava/lang/Object;)Ljava/lang/Object;")
    andThen = JavaMethod("(Ljava/util/function/Function;)Ljava/util/function/BiFunction;")

class ObjLongConsumer(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/function/ObjLongConsumer"
    accept = JavaMethod("(Ljava/lang/Object;J)V")

class LongToIntFunction(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/function/LongToIntFunction"
    applyAsInt = JavaMethod("(J)I")

class DoubleConsumer(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/function/DoubleConsumer"
    accept = JavaMethod("(D)V")
    andThen = JavaMethod("(Ljava/util/function/DoubleConsumer;)Ljava/util/function/DoubleConsumer;")

class LongConsumer(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/function/LongConsumer"
    accept = JavaMethod("(J)V")
    andThen = JavaMethod("(Ljava/util/function/LongConsumer;)Ljava/util/function/LongConsumer;")

class IntPredicate(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/function/IntPredicate"
    test = JavaMethod("(I)Z")
    negate = JavaMethod("()Ljava/util/function/IntPredicate;")
    and = JavaMethod("(Ljava/util/function/IntPredicate;)Ljava/util/function/IntPredicate;")
    or = JavaMethod("(Ljava/util/function/IntPredicate;)Ljava/util/function/IntPredicate;")

class BooleanSupplier(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/function/BooleanSupplier"
    getAsBoolean = JavaMethod("()Z")

class IntToLongFunction(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/function/IntToLongFunction"
    applyAsLong = JavaMethod("(I)J")

class LongPredicate(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/function/LongPredicate"
    test = JavaMethod("(J)Z")
    negate = JavaMethod("()Ljava/util/function/LongPredicate;")
    and = JavaMethod("(Ljava/util/function/LongPredicate;)Ljava/util/function/LongPredicate;")
    or = JavaMethod("(Ljava/util/function/LongPredicate;)Ljava/util/function/LongPredicate;")

class Function(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/function/Function"
    apply = JavaMethod("(Ljava/lang/Object;)Ljava/lang/Object;")
    identity = JavaStaticMethod("()Ljava/util/function/Function;")
    compose = JavaMethod("(Ljava/util/function/Function;)Ljava/util/function/Function;")
    andThen = JavaMethod("(Ljava/util/function/Function;)Ljava/util/function/Function;")

class ToLongBiFunction(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/function/ToLongBiFunction"
    applyAsLong = JavaMethod("(Ljava/lang/Object;Ljava/lang/Object;)J")

class BiConsumer(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/function/BiConsumer"
    accept = JavaMethod("(Ljava/lang/Object;Ljava/lang/Object;)V")
    andThen = JavaMethod("(Ljava/util/function/BiConsumer;)Ljava/util/function/BiConsumer;")

class IntUnaryOperator(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/function/IntUnaryOperator"
    identity = JavaStaticMethod("()Ljava/util/function/IntUnaryOperator;")
    applyAsInt = JavaMethod("(I)I")
    compose = JavaMethod("(Ljava/util/function/IntUnaryOperator;)Ljava/util/function/IntUnaryOperator;")
    andThen = JavaMethod("(Ljava/util/function/IntUnaryOperator;)Ljava/util/function/IntUnaryOperator;")

class DoubleFunction(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/function/DoubleFunction"
    apply = JavaMethod("(D)Ljava/lang/Object;")

class DoubleToLongFunction(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/function/DoubleToLongFunction"
    applyAsLong = JavaMethod("(D)J")

class ToLongFunction(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/function/ToLongFunction"
    applyAsLong = JavaMethod("(Ljava/lang/Object;)J")

class Consumer(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/function/Consumer"
    accept = JavaMethod("(Ljava/lang/Object;)V")
    andThen = JavaMethod("(Ljava/util/function/Consumer;)Ljava/util/function/Consumer;")

class IntSupplier(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/function/IntSupplier"
    getAsInt = JavaMethod("()I")

class DoubleToIntFunction(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/function/DoubleToIntFunction"
    applyAsInt = JavaMethod("(D)I")

class Predicate(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/function/Predicate"
    test = JavaMethod("(Ljava/lang/Object;)Z")
    negate = JavaMethod("()Ljava/util/function/Predicate;")
    and = JavaMethod("(Ljava/util/function/Predicate;)Ljava/util/function/Predicate;")
    not = JavaStaticMethod("(Ljava/util/function/Predicate;)Ljava/util/function/Predicate;")
    isEqual = JavaStaticMethod("(Ljava/lang/Object;)Ljava/util/function/Predicate;")
    or = JavaMethod("(Ljava/util/function/Predicate;)Ljava/util/function/Predicate;")

class ToDoubleFunction(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/function/ToDoubleFunction"
    applyAsDouble = JavaMethod("(Ljava/lang/Object;)D")