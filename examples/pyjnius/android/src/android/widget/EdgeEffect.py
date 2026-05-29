from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["EdgeEffect"]

class EdgeEffect(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/widget/EdgeEffect"
    __javaconstructor__ = [("(Landroid/content/Context;)V", False), ("(Landroid/content/Context;Landroid/util/AttributeSet;)V", False)]
    DEFAULT_BLEND_MODE = JavaStaticField("Landroid/graphics/BlendMode;")
    finish = JavaMethod("()V")
    getMaxHeight = JavaMethod("()I")
    draw = JavaMethod("(Landroid/graphics/Canvas;)Z")
    isFinished = JavaMethod("()Z")
    setBlendMode = JavaMethod("(Landroid/graphics/BlendMode;)V")
    setColor = JavaMethod("(I)V")
    getColor = JavaMethod("()I")
    getBlendMode = JavaMethod("()Landroid/graphics/BlendMode;")
    getDistance = JavaMethod("()F")
    onAbsorb = JavaMethod("(I)V")
    onPull = JavaMultipleMethod([("(F)V", False, False), ("(FF)V", False, False)])
    onPullDistance = JavaMethod("(FF)F")
    onRelease = JavaMethod("()V")
    setSize = JavaMethod("(II)V")