from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["PathMeasure"]

class PathMeasure(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/graphics/PathMeasure"
    __javaconstructor__ = [("()V", False), ("(Landroid/graphics/Path;Z)V", False)]
    POSITION_MATRIX_FLAG = JavaStaticField("I")
    TANGENT_MATRIX_FLAG = JavaStaticField("I")
    getSegment = JavaMethod("(FFLandroid/graphics/Path;Z)Z")
    nextContour = JavaMethod("()Z")
    getPosTan = JavaMethod("(F[F[F)Z")
    getLength = JavaMethod("()F")
    getMatrix = JavaMethod("(FLandroid/graphics/Matrix;I)Z")
    isClosed = JavaMethod("()Z")
    setPath = JavaMethod("(Landroid/graphics/Path;Z)V")