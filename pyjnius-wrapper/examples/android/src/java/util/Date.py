from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Date"]

class Date(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/Date"
    __javaconstructor__ = [("()V", False), ("(J)V", False), ("(III)V", False), ("(IIIII)V", False), ("(IIIIII)V", False), ("(Ljava/lang/String;)V", False)]
    clone = JavaMethod("()Ljava/lang/Object;")
    UTC = JavaStaticMethod("(IIIIII)J")
    parse = JavaStaticMethod("(Ljava/lang/String;)J")
    getYear = JavaMethod("()I")
    setYear = JavaMethod("(I)V")
    getMonth = JavaMethod("()I")
    setMonth = JavaMethod("(I)V")
    getDate = JavaMethod("()I")
    setDate = JavaMethod("(I)V")
    getDay = JavaMethod("()I")
    getHours = JavaMethod("()I")
    setHours = JavaMethod("(I)V")
    getMinutes = JavaMethod("()I")
    setMinutes = JavaMethod("(I)V")
    getSeconds = JavaMethod("()I")
    setSeconds = JavaMethod("(I)V")
    getTime = JavaMethod("()J")
    setTime = JavaMethod("(J)V")
    before = JavaMethod("(Ljava/util/Date;)Z")
    after = JavaMethod("(Ljava/util/Date;)Z")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    compareTo = JavaMethod("(Ljava/util/Date;)I")
    hashCode = JavaMethod("()I")
    toString = JavaMethod("()Ljava/lang/String;")
    toLocaleString = JavaMethod("()Ljava/lang/String;")
    toGMTString = JavaMethod("()Ljava/lang/String;")
    getTimezoneOffset = JavaMethod("()I")
    from = JavaStaticMethod("(Ljava/time/Instant;)Ljava/util/Date;")
    toInstant = JavaMethod("()Ljava/time/Instant;")