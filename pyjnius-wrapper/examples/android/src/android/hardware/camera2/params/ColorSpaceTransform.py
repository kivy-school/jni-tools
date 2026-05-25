from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ColorSpaceTransform"]

class ColorSpaceTransform(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/hardware/camera2/params/ColorSpaceTransform"
    __javaconstructor__ = [("([Landroid/util/Rational;)V", False), ("([I)V", False)]
    getElement = JavaMethod("(II)Landroid/util/Rational;")
    copyElements = JavaMultipleMethod([("([Landroid/util/Rational;I)V", False, False), ("([II)V", False, False)])
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    toString = JavaMethod("()Ljava/lang/String;")