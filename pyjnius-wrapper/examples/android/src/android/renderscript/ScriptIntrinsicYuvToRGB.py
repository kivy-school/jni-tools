from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ScriptIntrinsicYuvToRGB"]

class ScriptIntrinsicYuvToRGB(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/renderscript/ScriptIntrinsicYuvToRGB"
    create = JavaStaticMethod("(Landroid/renderscript/RenderScript;Landroid/renderscript/Element;)Landroid/renderscript/ScriptIntrinsicYuvToRGB;")
    setInput = JavaMethod("(Landroid/renderscript/Allocation;)V")
    forEach = JavaMethod("(Landroid/renderscript/Allocation;)V")
    getKernelID = JavaMethod("()Landroid/renderscript/Script$KernelID;")
    getFieldID_Input = JavaMethod("()Landroid/renderscript/Script$FieldID;")