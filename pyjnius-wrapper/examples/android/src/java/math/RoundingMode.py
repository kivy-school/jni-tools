from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["RoundingMode"]

class RoundingMode(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/math/RoundingMode"
    values = JavaStaticMethod("()[Ljava/math/RoundingMode;")
    valueOf = JavaMultipleMethod([("(Ljava/lang/String;)Ljava/math/RoundingMode;", True, False), ("(I)Ljava/math/RoundingMode;", True, False)])
    UP = JavaStaticField("Ljava/math/RoundingMode;")
    DOWN = JavaStaticField("Ljava/math/RoundingMode;")
    CEILING = JavaStaticField("Ljava/math/RoundingMode;")
    FLOOR = JavaStaticField("Ljava/math/RoundingMode;")
    HALF_UP = JavaStaticField("Ljava/math/RoundingMode;")
    HALF_DOWN = JavaStaticField("Ljava/math/RoundingMode;")
    HALF_EVEN = JavaStaticField("Ljava/math/RoundingMode;")
    UNNECESSARY = JavaStaticField("Ljava/math/RoundingMode;")