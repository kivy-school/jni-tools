from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Magnifier"]

class Magnifier(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/widget/Magnifier"
    __javaconstructor__ = [("(Landroid/view/View;)V", False)]
    SOURCE_BOUND_MAX_IN_SURFACE = JavaStaticField("I")
    SOURCE_BOUND_MAX_VISIBLE = JavaStaticField("I")
    update = JavaMethod("()V")
    getElevation = JavaMethod("()F")
    getHeight = JavaMethod("()I")
    getOverlay = JavaMethod("()Landroid/graphics/drawable/Drawable;")
    getWidth = JavaMethod("()I")
    show = JavaMultipleMethod([("(FFFF)V", False, False), ("(FF)V", False, False)])
    getPosition = JavaMethod("()Landroid/graphics/Point;")
    dismiss = JavaMethod("()V")
    isClippingEnabled = JavaMethod("()Z")
    getSourceHeight = JavaMethod("()I")
    getZoom = JavaMethod("()F")
    setZoom = JavaMethod("(F)V")
    getSourceWidth = JavaMethod("()I")
    getSourcePosition = JavaMethod("()Landroid/graphics/Point;")
    getCornerRadius = JavaMethod("()F")
    getDefaultHorizontalSourceToMagnifierOffset = JavaMethod("()I")
    getDefaultVerticalSourceToMagnifierOffset = JavaMethod("()I")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/widget/Magnifier$Builder"
        __javaconstructor__ = [("(Landroid/view/View;)V", False)]
        setElevation = JavaMethod("(F)Landroid/widget/Magnifier$Builder;")
        setInitialZoom = JavaMethod("(F)Landroid/widget/Magnifier$Builder;")
        setOverlay = JavaMethod("(Landroid/graphics/drawable/Drawable;)Landroid/widget/Magnifier$Builder;")
        setCornerRadius = JavaMethod("(F)Landroid/widget/Magnifier$Builder;")
        setDefaultSourceToMagnifierOffset = JavaMethod("(II)Landroid/widget/Magnifier$Builder;")
        setSourceBounds = JavaMethod("(IIII)Landroid/widget/Magnifier$Builder;")
        build = JavaMethod("()Landroid/widget/Magnifier;")
        setClippingEnabled = JavaMethod("(Z)Landroid/widget/Magnifier$Builder;")
        setSize = JavaMethod("(II)Landroid/widget/Magnifier$Builder;")