from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Script"]

class Script(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/renderscript/Script"
    getVarD = JavaMethod("(I)D")
    bindAllocation = JavaMethod("(Landroid/renderscript/Allocation;I)V")
    getVarB = JavaMethod("(I)Z")
    getVarF = JavaMethod("(I)F")
    getVarI = JavaMethod("(I)I")
    getVarJ = JavaMethod("(I)J")
    getVarV = JavaMethod("(ILandroid/renderscript/FieldPacker;)V")
    setVar = JavaMultipleMethod([("(ILandroid/renderscript/BaseObj;)V", False, False), ("(ILandroid/renderscript/FieldPacker;)V", False, False), ("(ILandroid/renderscript/FieldPacker;Landroid/renderscript/Element;[I)V", False, False), ("(II)V", False, False), ("(IF)V", False, False), ("(ID)V", False, False), ("(IZ)V", False, False), ("(IJ)V", False, False)])
    setTimeZone = JavaMethod("(Ljava/lang/String;)V")

    class LaunchOptions(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/renderscript/Script$LaunchOptions"
        __javaconstructor__ = [("()V", False)]
        getYStart = JavaMethod("()I")
        getZStart = JavaMethod("()I")
        getXEnd = JavaMethod("()I")
        getYEnd = JavaMethod("()I")
        getZEnd = JavaMethod("()I")
        getXStart = JavaMethod("()I")
        setX = JavaMethod("(II)Landroid/renderscript/Script$LaunchOptions;")
        setY = JavaMethod("(II)Landroid/renderscript/Script$LaunchOptions;")
        setZ = JavaMethod("(II)Landroid/renderscript/Script$LaunchOptions;")

    class KernelID(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/renderscript/Script$KernelID"

    class InvokeID(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/renderscript/Script$InvokeID"

    class FieldID(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/renderscript/Script$FieldID"

    class FieldBase(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/renderscript/Script$FieldBase"
        updateAllocation = JavaMethod("()V")
        getAllocation = JavaMethod("()Landroid/renderscript/Allocation;")
        getType = JavaMethod("()Landroid/renderscript/Type;")
        getElement = JavaMethod("()Landroid/renderscript/Element;")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/renderscript/Script$Builder"