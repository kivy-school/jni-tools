from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["MeshSpecification"]

class MeshSpecification(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/graphics/MeshSpecification"
    ALPHA_TYPE_OPAQUE = JavaStaticField("I")
    ALPHA_TYPE_PREMULTIPLIED = JavaStaticField("I")
    ALPHA_TYPE_UNKNOWN = JavaStaticField("I")
    ALPHA_TYPE_UNPREMULTIPLIED = JavaStaticField("I")
    TYPE_FLOAT = JavaStaticField("I")
    TYPE_FLOAT2 = JavaStaticField("I")
    TYPE_FLOAT3 = JavaStaticField("I")
    TYPE_FLOAT4 = JavaStaticField("I")
    TYPE_UBYTE4 = JavaStaticField("I")
    make = JavaMultipleMethod([("([Landroid/graphics/MeshSpecification$Attribute;I[Landroid/graphics/MeshSpecification$Varying;Ljava/lang/String;Ljava/lang/String;)Landroid/graphics/MeshSpecification;", True, False), ("([Landroid/graphics/MeshSpecification$Attribute;I[Landroid/graphics/MeshSpecification$Varying;Ljava/lang/String;Ljava/lang/String;Landroid/graphics/ColorSpace;)Landroid/graphics/MeshSpecification;", True, False), ("([Landroid/graphics/MeshSpecification$Attribute;I[Landroid/graphics/MeshSpecification$Varying;Ljava/lang/String;Ljava/lang/String;Landroid/graphics/ColorSpace;I)Landroid/graphics/MeshSpecification;", True, False)])

    class Attribute(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/graphics/MeshSpecification/Attribute"
        __javaconstructor__ = [("(IILjava/lang/String;)V", False)]
        getType = JavaMethod("()I")
        getOffset = JavaMethod("()I")
        getName = JavaMethod("()Ljava/lang/String;")
        toString = JavaMethod("()Ljava/lang/String;")

    class Varying(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/graphics/MeshSpecification/Varying"
        __javaconstructor__ = [("(ILjava/lang/String;)V", False)]
        getType = JavaMethod("()I")
        getName = JavaMethod("()Ljava/lang/String;")
        toString = JavaMethod("()Ljava/lang/String;")