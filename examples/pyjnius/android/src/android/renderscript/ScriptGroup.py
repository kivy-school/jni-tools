from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ScriptGroup"]

class ScriptGroup(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/renderscript/ScriptGroup"
    setOutput = JavaMethod("(Landroid/renderscript/Script$KernelID;Landroid/renderscript/Allocation;)V")
    destroy = JavaMethod("()V")
    execute = JavaMultipleMethod([("([Ljava/lang/Object;)[Ljava/lang/Object;", False, True), ("()V", False, False)])
    setInput = JavaMethod("(Landroid/renderscript/Script$KernelID;Landroid/renderscript/Allocation;)V")

    class Input(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/renderscript/ScriptGroup$Input"

    class Future(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/renderscript/ScriptGroup$Future"

    class Closure(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/renderscript/ScriptGroup$Closure"
        getGlobal = JavaMethod("(Landroid/renderscript/Script$FieldID;)Landroid/renderscript/ScriptGroup$Future;")
        getReturn = JavaMethod("()Landroid/renderscript/ScriptGroup$Future;")
        destroy = JavaMethod("()V")

    class Builder2(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/renderscript/ScriptGroup$Builder2"
        __javaconstructor__ = [("(Landroid/renderscript/RenderScript;)V", False)]
        addKernel = JavaMethod("(Landroid/renderscript/Script$KernelID;Landroid/renderscript/Type;[Ljava/lang/Object;)Landroid/renderscript/ScriptGroup$Closure;", varargs=True)
        addInvoke = JavaMethod("(Landroid/renderscript/Script$InvokeID;[Ljava/lang/Object;)Landroid/renderscript/ScriptGroup$Closure;", varargs=True)
        addInput = JavaMethod("()Landroid/renderscript/ScriptGroup$Input;")
        create = JavaMethod("(Ljava/lang/String;[Landroid/renderscript/ScriptGroup$Future;)Landroid/renderscript/ScriptGroup;", varargs=True)

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/renderscript/ScriptGroup$Builder"
        __javaconstructor__ = [("(Landroid/renderscript/RenderScript;)V", False)]
        addKernel = JavaMethod("(Landroid/renderscript/Script$KernelID;)Landroid/renderscript/ScriptGroup$Builder;")
        addConnection = JavaMultipleMethod([("(Landroid/renderscript/Type;Landroid/renderscript/Script$KernelID;Landroid/renderscript/Script$FieldID;)Landroid/renderscript/ScriptGroup$Builder;", False, False), ("(Landroid/renderscript/Type;Landroid/renderscript/Script$KernelID;Landroid/renderscript/Script$KernelID;)Landroid/renderscript/ScriptGroup$Builder;", False, False)])
        create = JavaMethod("()Landroid/renderscript/ScriptGroup;")

    class Binding(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/renderscript/ScriptGroup$Binding"
        __javaconstructor__ = [("(Landroid/renderscript/Script$FieldID;Ljava/lang/Object;)V", False)]