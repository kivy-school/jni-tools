from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Matrix"]

class Matrix(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/opengl/Matrix"
    __javaconstructor__ = [("()V", False)]
    frustumM = JavaStaticMethod("([FIFFFFFF)V")
    multiplyMV = JavaStaticMethod("([FI[FI[FI)V")
    invertM = JavaStaticMethod("([FI[FI)Z")
    orthoM = JavaStaticMethod("([FIFFFFFF)V")
    perspectiveM = JavaStaticMethod("([FIFFFF)V")
    rotateM = JavaMultipleMethod([("([FIFFFF)V", True, False), ("([FI[FIFFFF)V", True, False)])
    scaleM = JavaMultipleMethod([("([FI[FIFFF)V", True, False), ("([FIFFF)V", True, False)])
    multiplyMM = JavaStaticMethod("([FI[FI[FI)V")
    setIdentityM = JavaStaticMethod("([FI)V")
    setLookAtM = JavaStaticMethod("([FIFFFFFFFFF)V")
    setRotateEulerM = JavaStaticMethod("([FIFFF)V")
    setRotateEulerM2 = JavaStaticMethod("([FIFFF)V")
    setRotateM = JavaStaticMethod("([FIFFFF)V")
    translateM = JavaMultipleMethod([("([FIFFF)V", True, False), ("([FI[FIFFF)V", True, False)])
    transposeM = JavaStaticMethod("([FI[FI)V")
    length = JavaStaticMethod("(FFF)F")