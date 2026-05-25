from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Optional"]

class Optional(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/Optional"
    empty = JavaStaticMethod("()Ljava/util/Optional;")
    of = JavaStaticMethod("(Ljava/lang/Object;)Ljava/util/Optional;")
    ofNullable = JavaStaticMethod("(Ljava/lang/Object;)Ljava/util/Optional;")
    get = JavaMethod("()Ljava/lang/Object;")
    isPresent = JavaMethod("()Z")
    isEmpty = JavaMethod("()Z")
    ifPresent = JavaMethod("(Ljava/util/function/Consumer;)V")
    ifPresentOrElse = JavaMethod("(Ljava/util/function/Consumer;Ljava/lang/Runnable;)V")
    filter = JavaMethod("(Ljava/util/function/Predicate;)Ljava/util/Optional;")
    map = JavaMethod("(Ljava/util/function/Function;)Ljava/util/Optional;")
    flatMap = JavaMethod("(Ljava/util/function/Function;)Ljava/util/Optional;")
    or = JavaMethod("(Ljava/util/function/Supplier;)Ljava/util/Optional;")
    stream = JavaMethod("()Ljava/util/stream/Stream;")
    orElse = JavaMethod("(Ljava/lang/Object;)Ljava/lang/Object;")
    orElseGet = JavaMethod("(Ljava/util/function/Supplier;)Ljava/lang/Object;")
    orElseThrow = JavaMultipleMethod([("()Ljava/lang/Object;", False, False), ("(Ljava/util/function/Supplier;)Ljava/lang/Object;", False, False)])
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    toString = JavaMethod("()Ljava/lang/String;")