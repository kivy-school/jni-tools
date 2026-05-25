from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ScriptIntrinsicConvolve5x5"]

class ScriptIntrinsicConvolve5x5(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/renderscript/ScriptIntrinsicConvolve5x5"
    create = JavaStaticMethod("(Landroid/renderscript/RenderScript;Landroid/renderscript/Element;)Landroid/renderscript/ScriptIntrinsicConvolve5x5;")
    setInput = JavaMethod("(Landroid/renderscript/Allocation;)V")
    setCoefficients = JavaMethod("([F)V")
    forEach = JavaMultipleMethod([("(Landroid/renderscript/Allocation;)V", False, False), ("(Landroid/renderscript/Allocation;Landroid/renderscript/Script$LaunchOptions;)V", False, False)])
    getKernelID = JavaMethod("()Landroid/renderscript/Script$KernelID;")
    getFieldID_Input = JavaMethod("()Landroid/renderscript/Script$FieldID;")