from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Script"]

class Script(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/renderscript/Script"
    createKernelID = JavaMethod("(IILandroid/renderscript/Element;Landroid/renderscript/Element;)Landroid/renderscript/Script$KernelID;")
    createInvokeID = JavaMethod("(I)Landroid/renderscript/Script$InvokeID;")
    createFieldID = JavaMethod("(ILandroid/renderscript/Element;)Landroid/renderscript/Script$FieldID;")
    invoke = JavaMultipleMethod([("(I)V", False, False), ("(ILandroid/renderscript/FieldPacker;)V", False, False)])
    forEach = JavaMultipleMethod([("(ILandroid/renderscript/Allocation;Landroid/renderscript/Allocation;Landroid/renderscript/FieldPacker;)V", False, False), ("(ILandroid/renderscript/Allocation;Landroid/renderscript/Allocation;Landroid/renderscript/FieldPacker;Landroid/renderscript/Script$LaunchOptions;)V", False, False), ("(I[Landroid/renderscript/Allocation;Landroid/renderscript/Allocation;Landroid/renderscript/FieldPacker;)V", False, False), ("(I[Landroid/renderscript/Allocation;Landroid/renderscript/Allocation;Landroid/renderscript/FieldPacker;Landroid/renderscript/Script$LaunchOptions;)V", False, False)])
    reduce = JavaMethod("(I[Landroid/renderscript/Allocation;Landroid/renderscript/Allocation;Landroid/renderscript/Script$LaunchOptions;)V")
    bindAllocation = JavaMethod("(Landroid/renderscript/Allocation;I)V")
    setVar = JavaMultipleMethod([("(IF)V", False, False), ("(ID)V", False, False), ("(II)V", False, False), ("(IJ)V", False, False), ("(IZ)V", False, False), ("(ILandroid/renderscript/BaseObj;)V", False, False), ("(ILandroid/renderscript/FieldPacker;)V", False, False), ("(ILandroid/renderscript/FieldPacker;Landroid/renderscript/Element;[I)V", False, False)])
    getVarF = JavaMethod("(I)F")
    getVarD = JavaMethod("(I)D")
    getVarI = JavaMethod("(I)I")
    getVarJ = JavaMethod("(I)J")
    getVarB = JavaMethod("(I)Z")
    getVarV = JavaMethod("(ILandroid/renderscript/FieldPacker;)V")
    setTimeZone = JavaMethod("(Ljava/lang/String;)V")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/renderscript/Script/Builder"

    class FieldBase(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/renderscript/Script/FieldBase"
        __javaconstructor__ = [("()V", False)]
        mAllocation = JavaField("Landroid/renderscript/Allocation;")
        mElement = JavaField("Landroid/renderscript/Element;")
        init = JavaMultipleMethod([("(Landroid/renderscript/RenderScript;I)V", False, False), ("(Landroid/renderscript/RenderScript;II)V", False, False)])
        getElement = JavaMethod("()Landroid/renderscript/Element;")
        getType = JavaMethod("()Landroid/renderscript/Type;")
        getAllocation = JavaMethod("()Landroid/renderscript/Allocation;")
        updateAllocation = JavaMethod("()V")

    class FieldID(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/renderscript/Script/FieldID"

    class InvokeID(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/renderscript/Script/InvokeID"

    class KernelID(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/renderscript/Script/KernelID"

    class LaunchOptions(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/renderscript/Script/LaunchOptions"
        __javaconstructor__ = [("()V", False)]
        setX = JavaMethod("(II)Landroid/renderscript/Script$LaunchOptions;")
        setY = JavaMethod("(II)Landroid/renderscript/Script$LaunchOptions;")
        setZ = JavaMethod("(II)Landroid/renderscript/Script$LaunchOptions;")
        getXStart = JavaMethod("()I")
        getXEnd = JavaMethod("()I")
        getYStart = JavaMethod("()I")
        getYEnd = JavaMethod("()I")
        getZStart = JavaMethod("()I")
        getZEnd = JavaMethod("()I")