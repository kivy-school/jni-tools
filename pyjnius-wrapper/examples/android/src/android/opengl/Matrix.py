from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Matrix"]

class Matrix(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/opengl/Matrix"
    __javaconstructor__ = [("()V", False)]
    multiplyMM = JavaStaticMethod("([FI[FI[FI)V")
    multiplyMV = JavaStaticMethod("([FI[FI[FI)V")
    transposeM = JavaStaticMethod("([FI[FI)V")
    invertM = JavaStaticMethod("([FI[FI)Z")
    orthoM = JavaStaticMethod("([FIFFFFFF)V")
    frustumM = JavaStaticMethod("([FIFFFFFF)V")
    perspectiveM = JavaStaticMethod("([FIFFFF)V")
    length = JavaStaticMethod("(FFF)F")
    setIdentityM = JavaStaticMethod("([FI)V")
    scaleM = JavaMultipleMethod([("([FI[FIFFF)V", True, False), ("([FIFFF)V", True, False)])
    translateM = JavaMultipleMethod([("([FI[FIFFF)V", True, False), ("([FIFFF)V", True, False)])
    rotateM = JavaMultipleMethod([("([FI[FIFFFF)V", True, False), ("([FIFFFF)V", True, False)])
    setRotateM = JavaStaticMethod("([FIFFFF)V")
    setRotateEulerM = JavaStaticMethod("([FIFFF)V")
    setRotateEulerM2 = JavaStaticMethod("([FIFFF)V")
    setLookAtM = JavaStaticMethod("([FIFFFFFFFFF)V")