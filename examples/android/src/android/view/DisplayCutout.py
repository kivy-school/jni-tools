from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["DisplayCutout"]

class DisplayCutout(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/view/DisplayCutout"
    __javaconstructor__ = [("(Landroid/graphics/Insets;Landroid/graphics/Rect;Landroid/graphics/Rect;Landroid/graphics/Rect;Landroid/graphics/Rect;)V", False), ("(Landroid/graphics/Insets;Landroid/graphics/Rect;Landroid/graphics/Rect;Landroid/graphics/Rect;Landroid/graphics/Rect;Landroid/graphics/Insets;)V", False), ("(Landroid/graphics/Rect;Ljava/util/List;)V", False)]
    getWaterfallInsets = JavaMethod("()Landroid/graphics/Insets;")
    getSafeInsetTop = JavaMethod("()I")
    getSafeInsetBottom = JavaMethod("()I")
    getSafeInsetLeft = JavaMethod("()I")
    getSafeInsetRight = JavaMethod("()I")
    getBoundingRects = JavaMethod("()Ljava/util/List;")
    getBoundingRectLeft = JavaMethod("()Landroid/graphics/Rect;")
    getBoundingRectTop = JavaMethod("()Landroid/graphics/Rect;")
    getBoundingRectRight = JavaMethod("()Landroid/graphics/Rect;")
    getBoundingRectBottom = JavaMethod("()Landroid/graphics/Rect;")
    getCutoutPath = JavaMethod("()Landroid/graphics/Path;")
    hashCode = JavaMethod("()I")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/view/DisplayCutout/Builder"
        __javaconstructor__ = [("()V", False)]
        build = JavaMethod("()Landroid/view/DisplayCutout;")
        setSafeInsets = JavaMethod("(Landroid/graphics/Insets;)Landroid/view/DisplayCutout$Builder;")
        setWaterfallInsets = JavaMethod("(Landroid/graphics/Insets;)Landroid/view/DisplayCutout$Builder;")
        setBoundingRectLeft = JavaMethod("(Landroid/graphics/Rect;)Landroid/view/DisplayCutout$Builder;")
        setBoundingRectTop = JavaMethod("(Landroid/graphics/Rect;)Landroid/view/DisplayCutout$Builder;")
        setBoundingRectRight = JavaMethod("(Landroid/graphics/Rect;)Landroid/view/DisplayCutout$Builder;")
        setBoundingRectBottom = JavaMethod("(Landroid/graphics/Rect;)Landroid/view/DisplayCutout$Builder;")
        setCutoutPath = JavaMethod("(Landroid/graphics/Path;)Landroid/view/DisplayCutout$Builder;")