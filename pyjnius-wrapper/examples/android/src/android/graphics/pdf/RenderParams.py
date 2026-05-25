from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["RenderParams"]

class RenderParams(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/graphics/pdf/RenderParams"
    FLAG_RENDER_HIGHLIGHT_ANNOTATIONS = JavaStaticField("I")
    FLAG_RENDER_TEXT_ANNOTATIONS = JavaStaticField("I")
    RENDER_MODE_FOR_DISPLAY = JavaStaticField("I")
    RENDER_MODE_FOR_PRINT = JavaStaticField("I")
    getRenderMode = JavaMethod("()I")
    getRenderFlags = JavaMethod("()I")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/graphics/pdf/RenderParams/Builder"
        __javaconstructor__ = [("(I)V", False)]
        setRenderFlags = JavaMultipleMethod([("(I)Landroid/graphics/pdf/RenderParams$Builder;", False, False), ("(II)Landroid/graphics/pdf/RenderParams$Builder;", False, False)])
        build = JavaMethod("()Landroid/graphics/pdf/RenderParams;")