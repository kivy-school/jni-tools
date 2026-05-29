from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["EdgeEffect"]

class EdgeEffect(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/widget/EdgeEffect"
    __javaconstructor__ = [("(Landroid/content/Context;)V", False), ("(Landroid/content/Context;Landroid/util/AttributeSet;)V", False)]
    DEFAULT_BLEND_MODE = JavaStaticField("Landroid/graphics/BlendMode;")
    setSize = JavaMethod("(II)V")
    isFinished = JavaMethod("()Z")
    finish = JavaMethod("()V")
    onPull = JavaMultipleMethod([("(F)V", False, False), ("(FF)V", False, False)])
    onPullDistance = JavaMethod("(FF)F")
    getDistance = JavaMethod("()F")
    onRelease = JavaMethod("()V")
    onAbsorb = JavaMethod("(I)V")
    setColor = JavaMethod("(I)V")
    setBlendMode = JavaMethod("(Landroid/graphics/BlendMode;)V")
    getColor = JavaMethod("()I")
    getBlendMode = JavaMethod("()Landroid/graphics/BlendMode;")
    draw = JavaMethod("(Landroid/graphics/Canvas;)Z")
    getMaxHeight = JavaMethod("()I")