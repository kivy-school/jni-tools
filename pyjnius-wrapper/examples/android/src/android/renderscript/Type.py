from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Type"]

class Type(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/renderscript/Type"
    getElement = JavaMethod("()Landroid/renderscript/Element;")
    getX = JavaMethod("()I")
    getY = JavaMethod("()I")
    getZ = JavaMethod("()I")
    getYuv = JavaMethod("()I")
    hasMipmaps = JavaMethod("()Z")
    hasFaces = JavaMethod("()Z")
    getCount = JavaMethod("()I")
    createX = JavaStaticMethod("(Landroid/renderscript/RenderScript;Landroid/renderscript/Element;I)Landroid/renderscript/Type;")
    createXY = JavaStaticMethod("(Landroid/renderscript/RenderScript;Landroid/renderscript/Element;II)Landroid/renderscript/Type;")
    createXYZ = JavaStaticMethod("(Landroid/renderscript/RenderScript;Landroid/renderscript/Element;III)Landroid/renderscript/Type;")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/renderscript/Type/Builder"
        __javaconstructor__ = [("(Landroid/renderscript/RenderScript;Landroid/renderscript/Element;)V", False)]
        setX = JavaMethod("(I)Landroid/renderscript/Type$Builder;")
        setY = JavaMethod("(I)Landroid/renderscript/Type$Builder;")
        setZ = JavaMethod("(I)Landroid/renderscript/Type$Builder;")
        setMipmaps = JavaMethod("(Z)Landroid/renderscript/Type$Builder;")
        setFaces = JavaMethod("(Z)Landroid/renderscript/Type$Builder;")
        setYuvFormat = JavaMethod("(I)Landroid/renderscript/Type$Builder;")
        create = JavaMethod("()Landroid/renderscript/Type;")

    class CubemapFace(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/renderscript/Type/CubemapFace"
        values = JavaStaticMethod("()[Landroid/renderscript/Type$CubemapFace;")
        valueOf = JavaStaticMethod("(Ljava/lang/String;)Landroid/renderscript/Type$CubemapFace;")
        POSITIVE_X = JavaStaticField("Landroid/renderscript/Type/CubemapFace;")
        NEGATIVE_X = JavaStaticField("Landroid/renderscript/Type/CubemapFace;")
        POSITIVE_Y = JavaStaticField("Landroid/renderscript/Type/CubemapFace;")
        NEGATIVE_Y = JavaStaticField("Landroid/renderscript/Type/CubemapFace;")
        POSITIVE_Z = JavaStaticField("Landroid/renderscript/Type/CubemapFace;")
        NEGATIVE_Z = JavaStaticField("Landroid/renderscript/Type/CubemapFace;")
        POSITVE_X = JavaStaticField("Landroid/renderscript/Type/CubemapFace;")
        POSITVE_Y = JavaStaticField("Landroid/renderscript/Type/CubemapFace;")
        POSITVE_Z = JavaStaticField("Landroid/renderscript/Type/CubemapFace;")