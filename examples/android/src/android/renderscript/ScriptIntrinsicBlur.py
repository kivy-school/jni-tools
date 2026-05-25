from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ScriptIntrinsicBlur"]

class ScriptIntrinsicBlur(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/renderscript/ScriptIntrinsicBlur"
    create = JavaStaticMethod("(Landroid/renderscript/RenderScript;Landroid/renderscript/Element;)Landroid/renderscript/ScriptIntrinsicBlur;")
    setInput = JavaMethod("(Landroid/renderscript/Allocation;)V")
    setRadius = JavaMethod("(F)V")
    forEach = JavaMultipleMethod([("(Landroid/renderscript/Allocation;)V", False, False), ("(Landroid/renderscript/Allocation;Landroid/renderscript/Script$LaunchOptions;)V", False, False)])
    getKernelID = JavaMethod("()Landroid/renderscript/Script$KernelID;")
    getFieldID_Input = JavaMethod("()Landroid/renderscript/Script$FieldID;")