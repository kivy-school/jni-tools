from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ScriptIntrinsicHistogram"]

class ScriptIntrinsicHistogram(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/renderscript/ScriptIntrinsicHistogram"
    setOutput = JavaMethod("(Landroid/renderscript/Allocation;)V")
    setDotCoefficients = JavaMethod("(FFFF)V")
    getFieldID_Input = JavaMethod("()Landroid/renderscript/Script$FieldID;")
    forEach_Dot = JavaMultipleMethod([("(Landroid/renderscript/Allocation;Landroid/renderscript/Script$LaunchOptions;)V", False, False), ("(Landroid/renderscript/Allocation;)V", False, False)])
    getKernelID_Separate = JavaMethod("()Landroid/renderscript/Script$KernelID;")
    forEach = JavaMultipleMethod([("(Landroid/renderscript/Allocation;)V", False, False), ("(Landroid/renderscript/Allocation;Landroid/renderscript/Script$LaunchOptions;)V", False, False)])
    create = JavaStaticMethod("(Landroid/renderscript/RenderScript;Landroid/renderscript/Element;)Landroid/renderscript/ScriptIntrinsicHistogram;")