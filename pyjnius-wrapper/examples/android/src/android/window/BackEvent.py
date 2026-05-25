from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["BackEvent"]

class BackEvent(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/window/BackEvent"
    __javaconstructor__ = [("(FFFI)V", False)]
    EDGE_LEFT = JavaStaticField("I")
    EDGE_RIGHT = JavaStaticField("I")
    getProgress = JavaMethod("()F")
    getTouchX = JavaMethod("()F")
    getTouchY = JavaMethod("()F")
    getSwipeEdge = JavaMethod("()I")
    toString = JavaMethod("()Ljava/lang/String;")