from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Visibility"]

class Visibility(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/opengl/Visibility"
    __javaconstructor__ = [("()V", False)]
    visibilityTest = JavaStaticMethod("([FI[FI[CII)I")
    computeBoundingSphere = JavaStaticMethod("([FII[FI)V")
    frustumCullSpheres = JavaStaticMethod("([FI[FII[III)I")