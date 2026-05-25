from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["GridLayoutAnimationController"]

class GridLayoutAnimationController(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/view/animation/GridLayoutAnimationController"
    __javaconstructor__ = [("(Landroid/content/Context;Landroid/util/AttributeSet;)V", False), ("(Landroid/view/animation/Animation;)V", False), ("(Landroid/view/animation/Animation;FF)V", False)]
    DIRECTION_BOTTOM_TO_TOP = JavaStaticField("I")
    DIRECTION_HORIZONTAL_MASK = JavaStaticField("I")
    DIRECTION_LEFT_TO_RIGHT = JavaStaticField("I")
    DIRECTION_RIGHT_TO_LEFT = JavaStaticField("I")
    DIRECTION_TOP_TO_BOTTOM = JavaStaticField("I")
    DIRECTION_VERTICAL_MASK = JavaStaticField("I")
    PRIORITY_COLUMN = JavaStaticField("I")
    PRIORITY_NONE = JavaStaticField("I")
    PRIORITY_ROW = JavaStaticField("I")
    getColumnDelay = JavaMethod("()F")
    setColumnDelay = JavaMethod("(F)V")
    getRowDelay = JavaMethod("()F")
    setRowDelay = JavaMethod("(F)V")
    getDirection = JavaMethod("()I")
    setDirection = JavaMethod("(I)V")
    getDirectionPriority = JavaMethod("()I")
    setDirectionPriority = JavaMethod("(I)V")
    willOverlap = JavaMethod("()Z")
    getDelayForView = JavaMethod("(Landroid/view/View;)J")

    class AnimationParameters(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/view/animation/GridLayoutAnimationController/AnimationParameters"
        __javaconstructor__ = [("()V", False)]
        column = JavaField("I")
        columnsCount = JavaField("I")
        row = JavaField("I")
        rowsCount = JavaField("I")