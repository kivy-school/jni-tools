from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Magnifier"]

class Magnifier(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/widget/Magnifier"
    __javaconstructor__ = [("(Landroid/view/View;)V", False)]
    SOURCE_BOUND_MAX_IN_SURFACE = JavaStaticField("I")
    SOURCE_BOUND_MAX_VISIBLE = JavaStaticField("I")
    show = JavaMultipleMethod([("(FF)V", False, False), ("(FFFF)V", False, False)])
    dismiss = JavaMethod("()V")
    update = JavaMethod("()V")
    getWidth = JavaMethod("()I")
    getHeight = JavaMethod("()I")
    getSourceWidth = JavaMethod("()I")
    getSourceHeight = JavaMethod("()I")
    setZoom = JavaMethod("(F)V")
    getZoom = JavaMethod("()F")
    getElevation = JavaMethod("()F")
    getCornerRadius = JavaMethod("()F")
    getDefaultHorizontalSourceToMagnifierOffset = JavaMethod("()I")
    getDefaultVerticalSourceToMagnifierOffset = JavaMethod("()I")
    getOverlay = JavaMethod("()Landroid/graphics/drawable/Drawable;")
    isClippingEnabled = JavaMethod("()Z")
    getPosition = JavaMethod("()Landroid/graphics/Point;")
    getSourcePosition = JavaMethod("()Landroid/graphics/Point;")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/widget/Magnifier/Builder"
        __javaconstructor__ = [("(Landroid/view/View;)V", False)]
        setSize = JavaMethod("(II)Landroid/widget/Magnifier$Builder;")
        setInitialZoom = JavaMethod("(F)Landroid/widget/Magnifier$Builder;")
        setElevation = JavaMethod("(F)Landroid/widget/Magnifier$Builder;")
        setCornerRadius = JavaMethod("(F)Landroid/widget/Magnifier$Builder;")
        setOverlay = JavaMethod("(Landroid/graphics/drawable/Drawable;)Landroid/widget/Magnifier$Builder;")
        setDefaultSourceToMagnifierOffset = JavaMethod("(II)Landroid/widget/Magnifier$Builder;")
        setClippingEnabled = JavaMethod("(Z)Landroid/widget/Magnifier$Builder;")
        setSourceBounds = JavaMethod("(IIII)Landroid/widget/Magnifier$Builder;")
        build = JavaMethod("()Landroid/widget/Magnifier;")