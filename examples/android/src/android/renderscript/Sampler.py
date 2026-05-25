from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Sampler"]

class Sampler(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/renderscript/Sampler"
    getMinification = JavaMethod("()Landroid/renderscript/Sampler$Value;")
    getMagnification = JavaMethod("()Landroid/renderscript/Sampler$Value;")
    getWrapS = JavaMethod("()Landroid/renderscript/Sampler$Value;")
    getWrapT = JavaMethod("()Landroid/renderscript/Sampler$Value;")
    getAnisotropy = JavaMethod("()F")
    CLAMP_NEAREST = JavaStaticMethod("(Landroid/renderscript/RenderScript;)Landroid/renderscript/Sampler;")
    CLAMP_LINEAR = JavaStaticMethod("(Landroid/renderscript/RenderScript;)Landroid/renderscript/Sampler;")
    CLAMP_LINEAR_MIP_LINEAR = JavaStaticMethod("(Landroid/renderscript/RenderScript;)Landroid/renderscript/Sampler;")
    WRAP_NEAREST = JavaStaticMethod("(Landroid/renderscript/RenderScript;)Landroid/renderscript/Sampler;")
    WRAP_LINEAR = JavaStaticMethod("(Landroid/renderscript/RenderScript;)Landroid/renderscript/Sampler;")
    WRAP_LINEAR_MIP_LINEAR = JavaStaticMethod("(Landroid/renderscript/RenderScript;)Landroid/renderscript/Sampler;")
    MIRRORED_REPEAT_NEAREST = JavaStaticMethod("(Landroid/renderscript/RenderScript;)Landroid/renderscript/Sampler;")
    MIRRORED_REPEAT_LINEAR = JavaStaticMethod("(Landroid/renderscript/RenderScript;)Landroid/renderscript/Sampler;")
    MIRRORED_REPEAT_LINEAR_MIP_LINEAR = JavaStaticMethod("(Landroid/renderscript/RenderScript;)Landroid/renderscript/Sampler;")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/renderscript/Sampler/Builder"
        __javaconstructor__ = [("(Landroid/renderscript/RenderScript;)V", False)]
        setMinification = JavaMethod("(Landroid/renderscript/Sampler$Value;)V")
        setMagnification = JavaMethod("(Landroid/renderscript/Sampler$Value;)V")
        setWrapS = JavaMethod("(Landroid/renderscript/Sampler$Value;)V")
        setWrapT = JavaMethod("(Landroid/renderscript/Sampler$Value;)V")
        setAnisotropy = JavaMethod("(F)V")
        create = JavaMethod("()Landroid/renderscript/Sampler;")

    class Value(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/renderscript/Sampler/Value"
        values = JavaStaticMethod("()[Landroid/renderscript/Sampler$Value;")
        valueOf = JavaStaticMethod("(Ljava/lang/String;)Landroid/renderscript/Sampler$Value;")
        NEAREST = JavaStaticField("Landroid/renderscript/Sampler/Value;")
        LINEAR = JavaStaticField("Landroid/renderscript/Sampler/Value;")
        LINEAR_MIP_LINEAR = JavaStaticField("Landroid/renderscript/Sampler/Value;")
        LINEAR_MIP_NEAREST = JavaStaticField("Landroid/renderscript/Sampler/Value;")
        WRAP = JavaStaticField("Landroid/renderscript/Sampler/Value;")
        CLAMP = JavaStaticField("Landroid/renderscript/Sampler/Value;")
        MIRRORED_REPEAT = JavaStaticField("Landroid/renderscript/Sampler/Value;")