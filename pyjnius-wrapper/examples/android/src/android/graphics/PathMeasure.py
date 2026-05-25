from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["PathMeasure"]

class PathMeasure(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/graphics/PathMeasure"
    __javaconstructor__ = [("()V", False), ("(Landroid/graphics/Path;Z)V", False)]
    POSITION_MATRIX_FLAG = JavaStaticField("I")
    TANGENT_MATRIX_FLAG = JavaStaticField("I")
    setPath = JavaMethod("(Landroid/graphics/Path;Z)V")
    getLength = JavaMethod("()F")
    getPosTan = JavaMethod("(F[F[F)Z")
    getMatrix = JavaMethod("(FLandroid/graphics/Matrix;I)Z")
    getSegment = JavaMethod("(FFLandroid/graphics/Path;Z)Z")
    isClosed = JavaMethod("()Z")
    nextContour = JavaMethod("()Z")
    finalize = JavaMethod("()V")