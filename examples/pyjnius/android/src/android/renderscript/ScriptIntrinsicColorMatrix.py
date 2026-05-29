from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ScriptIntrinsicColorMatrix"]

class ScriptIntrinsicColorMatrix(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/renderscript/ScriptIntrinsicColorMatrix"
    setRGBtoYUV = JavaMethod("()V")
    setColorMatrix = JavaMultipleMethod([("(Landroid/renderscript/Matrix3f;)V", False, False), ("(Landroid/renderscript/Matrix4f;)V", False, False)])
    setAdd = JavaMultipleMethod([("(FFFF)V", False, False), ("(Landroid/renderscript/Float4;)V", False, False)])
    setGreyscale = JavaMethod("()V")
    setYUVtoRGB = JavaMethod("()V")
    getKernelID = JavaMethod("()Landroid/renderscript/Script$KernelID;")
    forEach = JavaMultipleMethod([("(Landroid/renderscript/Allocation;Landroid/renderscript/Allocation;)V", False, False), ("(Landroid/renderscript/Allocation;Landroid/renderscript/Allocation;Landroid/renderscript/Script$LaunchOptions;)V", False, False)])
    create = JavaMultipleMethod([("(Landroid/renderscript/RenderScript;Landroid/renderscript/Element;)Landroid/renderscript/ScriptIntrinsicColorMatrix;", True, False), ("(Landroid/renderscript/RenderScript;)Landroid/renderscript/ScriptIntrinsicColorMatrix;", True, False)])