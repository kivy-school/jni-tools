from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ScriptIntrinsic3DLUT"]

class ScriptIntrinsic3DLUT(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/renderscript/ScriptIntrinsic3DLUT"
    setLUT = JavaMethod("(Landroid/renderscript/Allocation;)V")
    getKernelID = JavaMethod("()Landroid/renderscript/Script$KernelID;")
    forEach = JavaMultipleMethod([("(Landroid/renderscript/Allocation;Landroid/renderscript/Allocation;)V", False, False), ("(Landroid/renderscript/Allocation;Landroid/renderscript/Allocation;Landroid/renderscript/Script$LaunchOptions;)V", False, False)])
    create = JavaStaticMethod("(Landroid/renderscript/RenderScript;Landroid/renderscript/Element;)Landroid/renderscript/ScriptIntrinsic3DLUT;")