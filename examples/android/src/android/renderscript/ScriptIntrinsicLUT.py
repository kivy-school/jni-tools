from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ScriptIntrinsicLUT"]

class ScriptIntrinsicLUT(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/renderscript/ScriptIntrinsicLUT"
    create = JavaStaticMethod("(Landroid/renderscript/RenderScript;Landroid/renderscript/Element;)Landroid/renderscript/ScriptIntrinsicLUT;")
    destroy = JavaMethod("()V")
    setRed = JavaMethod("(II)V")
    setGreen = JavaMethod("(II)V")
    setBlue = JavaMethod("(II)V")
    setAlpha = JavaMethod("(II)V")
    forEach = JavaMultipleMethod([("(Landroid/renderscript/Allocation;Landroid/renderscript/Allocation;)V", False, False), ("(Landroid/renderscript/Allocation;Landroid/renderscript/Allocation;Landroid/renderscript/Script$LaunchOptions;)V", False, False)])
    getKernelID = JavaMethod("()Landroid/renderscript/Script$KernelID;")