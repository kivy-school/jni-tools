from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ScriptIntrinsicHistogram"]

class ScriptIntrinsicHistogram(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/renderscript/ScriptIntrinsicHistogram"
    create = JavaStaticMethod("(Landroid/renderscript/RenderScript;Landroid/renderscript/Element;)Landroid/renderscript/ScriptIntrinsicHistogram;")
    forEach = JavaMultipleMethod([("(Landroid/renderscript/Allocation;)V", False, False), ("(Landroid/renderscript/Allocation;Landroid/renderscript/Script$LaunchOptions;)V", False, False)])
    setDotCoefficients = JavaMethod("(FFFF)V")
    setOutput = JavaMethod("(Landroid/renderscript/Allocation;)V")
    forEach_Dot = JavaMultipleMethod([("(Landroid/renderscript/Allocation;)V", False, False), ("(Landroid/renderscript/Allocation;Landroid/renderscript/Script$LaunchOptions;)V", False, False)])
    getKernelID_Separate = JavaMethod("()Landroid/renderscript/Script$KernelID;")
    getFieldID_Input = JavaMethod("()Landroid/renderscript/Script$FieldID;")