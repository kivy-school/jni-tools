from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ScriptIntrinsicResize"]

class ScriptIntrinsicResize(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/renderscript/ScriptIntrinsicResize"
    getFieldID_Input = JavaMethod("()Landroid/renderscript/Script$FieldID;")
    forEach_bicubic = JavaMultipleMethod([("(Landroid/renderscript/Allocation;Landroid/renderscript/Script$LaunchOptions;)V", False, False), ("(Landroid/renderscript/Allocation;)V", False, False)])
    getKernelID_bicubic = JavaMethod("()Landroid/renderscript/Script$KernelID;")
    create = JavaStaticMethod("(Landroid/renderscript/RenderScript;)Landroid/renderscript/ScriptIntrinsicResize;")
    setInput = JavaMethod("(Landroid/renderscript/Allocation;)V")