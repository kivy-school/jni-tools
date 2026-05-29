from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ScriptIntrinsicLUT"]

class ScriptIntrinsicLUT(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/renderscript/ScriptIntrinsicLUT"
    setBlue = JavaMethod("(II)V")
    setGreen = JavaMethod("(II)V")
    getKernelID = JavaMethod("()Landroid/renderscript/Script$KernelID;")
    setRed = JavaMethod("(II)V")
    forEach = JavaMultipleMethod([("(Landroid/renderscript/Allocation;Landroid/renderscript/Allocation;Landroid/renderscript/Script$LaunchOptions;)V", False, False), ("(Landroid/renderscript/Allocation;Landroid/renderscript/Allocation;)V", False, False)])
    destroy = JavaMethod("()V")
    create = JavaStaticMethod("(Landroid/renderscript/RenderScript;Landroid/renderscript/Element;)Landroid/renderscript/ScriptIntrinsicLUT;")
    setAlpha = JavaMethod("(II)V")