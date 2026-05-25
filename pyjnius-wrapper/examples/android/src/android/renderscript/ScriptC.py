from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ScriptC"]

class ScriptC(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/renderscript/ScriptC"
    __javaconstructor__ = [("(ILandroid/renderscript/RenderScript;)V", False), ("(JLandroid/renderscript/RenderScript;)V", False), ("(Landroid/renderscript/RenderScript;Landroid/content/res/Resources;I)V", False), ("(Landroid/renderscript/RenderScript;Ljava/lang/String;[B[B)V", False)]