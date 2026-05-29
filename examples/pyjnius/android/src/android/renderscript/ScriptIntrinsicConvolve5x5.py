from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ScriptIntrinsicConvolve5x5"]

class ScriptIntrinsicConvolve5x5(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/renderscript/ScriptIntrinsicConvolve5x5"
    getKernelID = JavaMethod("()Landroid/renderscript/Script$KernelID;")
    getFieldID_Input = JavaMethod("()Landroid/renderscript/Script$FieldID;")
    forEach = JavaMultipleMethod([("(Landroid/renderscript/Allocation;Landroid/renderscript/Script$LaunchOptions;)V", False, False), ("(Landroid/renderscript/Allocation;)V", False, False)])
    create = JavaStaticMethod("(Landroid/renderscript/RenderScript;Landroid/renderscript/Element;)Landroid/renderscript/ScriptIntrinsicConvolve5x5;")
    setCoefficients = JavaMethod("([F)V")
    setInput = JavaMethod("(Landroid/renderscript/Allocation;)V")