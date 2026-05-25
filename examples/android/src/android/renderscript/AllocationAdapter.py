from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AllocationAdapter"]

class AllocationAdapter(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/renderscript/AllocationAdapter"
    setLOD = JavaMethod("(I)V")
    setFace = JavaMethod("(Landroid/renderscript/Type$CubemapFace;)V")
    setX = JavaMethod("(I)V")
    setY = JavaMethod("(I)V")
    setZ = JavaMethod("(I)V")
    create1D = JavaStaticMethod("(Landroid/renderscript/RenderScript;Landroid/renderscript/Allocation;)Landroid/renderscript/AllocationAdapter;")
    create2D = JavaStaticMethod("(Landroid/renderscript/RenderScript;Landroid/renderscript/Allocation;)Landroid/renderscript/AllocationAdapter;")
    createTyped = JavaStaticMethod("(Landroid/renderscript/RenderScript;Landroid/renderscript/Allocation;Landroid/renderscript/Type;)Landroid/renderscript/AllocationAdapter;")
    resize = JavaMethod("(I)V")