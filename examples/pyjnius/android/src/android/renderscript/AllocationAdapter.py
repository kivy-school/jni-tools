from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AllocationAdapter"]

class AllocationAdapter(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/renderscript/AllocationAdapter"
    USAGE_GRAPHICS_CONSTANTS = JavaStaticField("I")
    USAGE_GRAPHICS_RENDER_TARGET = JavaStaticField("I")
    USAGE_GRAPHICS_TEXTURE = JavaStaticField("I")
    USAGE_GRAPHICS_VERTEX = JavaStaticField("I")
    USAGE_IO_INPUT = JavaStaticField("I")
    USAGE_IO_OUTPUT = JavaStaticField("I")
    USAGE_SCRIPT = JavaStaticField("I")
    USAGE_SHARED = JavaStaticField("I")
    createTyped = JavaStaticMethod("(Landroid/renderscript/RenderScript;Landroid/renderscript/Allocation;Landroid/renderscript/Type;)Landroid/renderscript/AllocationAdapter;")
    create1D = JavaStaticMethod("(Landroid/renderscript/RenderScript;Landroid/renderscript/Allocation;)Landroid/renderscript/AllocationAdapter;")
    create2D = JavaStaticMethod("(Landroid/renderscript/RenderScript;Landroid/renderscript/Allocation;)Landroid/renderscript/AllocationAdapter;")
    setFace = JavaMethod("(Landroid/renderscript/Type$CubemapFace;)V")
    setLOD = JavaMethod("(I)V")
    setX = JavaMethod("(I)V")
    setY = JavaMethod("(I)V")
    setZ = JavaMethod("(I)V")
    resize = JavaMethod("(I)V")