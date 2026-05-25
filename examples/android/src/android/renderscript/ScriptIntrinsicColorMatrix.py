from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ScriptIntrinsicColorMatrix"]

class ScriptIntrinsicColorMatrix(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/renderscript/ScriptIntrinsicColorMatrix"
    create = JavaMultipleMethod([("(Landroid/renderscript/RenderScript;Landroid/renderscript/Element;)Landroid/renderscript/ScriptIntrinsicColorMatrix;", True, False), ("(Landroid/renderscript/RenderScript;)Landroid/renderscript/ScriptIntrinsicColorMatrix;", True, False)])
    setColorMatrix = JavaMultipleMethod([("(Landroid/renderscript/Matrix4f;)V", False, False), ("(Landroid/renderscript/Matrix3f;)V", False, False)])
    setAdd = JavaMultipleMethod([("(Landroid/renderscript/Float4;)V", False, False), ("(FFFF)V", False, False)])
    setGreyscale = JavaMethod("()V")
    setYUVtoRGB = JavaMethod("()V")
    setRGBtoYUV = JavaMethod("()V")
    forEach = JavaMultipleMethod([("(Landroid/renderscript/Allocation;Landroid/renderscript/Allocation;)V", False, False), ("(Landroid/renderscript/Allocation;Landroid/renderscript/Allocation;Landroid/renderscript/Script$LaunchOptions;)V", False, False)])
    getKernelID = JavaMethod("()Landroid/renderscript/Script$KernelID;")