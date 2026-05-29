from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Mesh"]

class Mesh(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/graphics/Mesh"
    __javaconstructor__ = [("(Landroid/graphics/MeshSpecification;ILjava/nio/Buffer;ILjava/nio/ShortBuffer;Landroid/graphics/RectF;)V", False), ("(Landroid/graphics/MeshSpecification;ILjava/nio/Buffer;ILandroid/graphics/RectF;)V", False)]
    TRIANGLES = JavaStaticField("I")
    TRIANGLE_STRIP = JavaStaticField("I")
    setFloatUniform = JavaMultipleMethod([("(Ljava/lang/String;FFFF)V", False, False), ("(Ljava/lang/String;F)V", False, False), ("(Ljava/lang/String;FF)V", False, False), ("(Ljava/lang/String;[F)V", False, False), ("(Ljava/lang/String;FFF)V", False, False)])
    setIntUniform = JavaMultipleMethod([("(Ljava/lang/String;I)V", False, False), ("(Ljava/lang/String;IIII)V", False, False), ("(Ljava/lang/String;III)V", False, False), ("(Ljava/lang/String;II)V", False, False), ("(Ljava/lang/String;[I)V", False, False)])
    setColorUniform = JavaMultipleMethod([("(Ljava/lang/String;Landroid/graphics/Color;)V", False, False), ("(Ljava/lang/String;I)V", False, False), ("(Ljava/lang/String;J)V", False, False)])