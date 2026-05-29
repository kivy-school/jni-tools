from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["FaceDetector"]

class FaceDetector(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/media/FaceDetector"
    __javaconstructor__ = [("(III)V", False)]
    findFaces = JavaMethod("(Landroid/graphics/Bitmap;[Landroid/media/FaceDetector$Face;)I")
    finalize = JavaMethod("()V")

    class Face(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/media/FaceDetector/Face"
        CONFIDENCE_THRESHOLD = JavaStaticField("F")
        EULER_X = JavaStaticField("I")
        EULER_Y = JavaStaticField("I")
        EULER_Z = JavaStaticField("I")
        confidence = JavaMethod("()F")
        getMidPoint = JavaMethod("(Landroid/graphics/PointF;)V")
        eyesDistance = JavaMethod("()F")
        pose = JavaMethod("(I)F")