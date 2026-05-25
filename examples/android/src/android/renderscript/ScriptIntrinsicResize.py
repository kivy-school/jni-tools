from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ScriptIntrinsicResize"]

class ScriptIntrinsicResize(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/renderscript/ScriptIntrinsicResize"
    create = JavaStaticMethod("(Landroid/renderscript/RenderScript;)Landroid/renderscript/ScriptIntrinsicResize;")
    setInput = JavaMethod("(Landroid/renderscript/Allocation;)V")
    getFieldID_Input = JavaMethod("()Landroid/renderscript/Script$FieldID;")
    forEach_bicubic = JavaMultipleMethod([("(Landroid/renderscript/Allocation;)V", False, False), ("(Landroid/renderscript/Allocation;Landroid/renderscript/Script$LaunchOptions;)V", False, False)])
    getKernelID_bicubic = JavaMethod("()Landroid/renderscript/Script$KernelID;")