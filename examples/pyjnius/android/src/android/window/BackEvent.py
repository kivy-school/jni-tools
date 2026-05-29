from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["BackEvent"]

class BackEvent(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/window/BackEvent"
    __javaconstructor__ = [("(FFFI)V", False), ("(FFFIJ)V", False)]
    EDGE_LEFT = JavaStaticField("I")
    EDGE_NONE = JavaStaticField("I")
    EDGE_RIGHT = JavaStaticField("I")
    getSwipeEdge = JavaMethod("()I")
    getTouchX = JavaMethod("()F")
    getFrameTimeMillis = JavaMethod("()J")
    getTouchY = JavaMethod("()F")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    getProgress = JavaMethod("()F")