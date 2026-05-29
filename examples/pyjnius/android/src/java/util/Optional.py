from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Optional"]

class Optional(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/Optional"
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    of = JavaStaticMethod("(Ljava/lang/Object;)Ljava/util/Optional;")
    isEmpty = JavaMethod("()Z")
    get = JavaMethod("()Ljava/lang/Object;")
    map = JavaMethod("(Ljava/util/function/Function;)Ljava/util/Optional;")
    stream = JavaMethod("()Ljava/util/stream/Stream;")
    filter = JavaMethod("(Ljava/util/function/Predicate;)Ljava/util/Optional;")
    empty = JavaStaticMethod("()Ljava/util/Optional;")
    orElse = JavaMethod("(Ljava/lang/Object;)Ljava/lang/Object;")
    isPresent = JavaMethod("()Z")
    orElseThrow = JavaMultipleMethod([("()Ljava/lang/Object;", False, False), ("(Ljava/util/function/Supplier;)Ljava/lang/Object;", False, False)])
    flatMap = JavaMethod("(Ljava/util/function/Function;)Ljava/util/Optional;")
    ifPresent = JavaMethod("(Ljava/util/function/Consumer;)V")
    ofNullable = JavaStaticMethod("(Ljava/lang/Object;)Ljava/util/Optional;")
    ifPresentOrElse = JavaMethod("(Ljava/util/function/Consumer;Ljava/lang/Runnable;)V")
    or = JavaMethod("(Ljava/util/function/Supplier;)Ljava/util/Optional;")
    orElseGet = JavaMethod("(Ljava/util/function/Supplier;)Ljava/lang/Object;")