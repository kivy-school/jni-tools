from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["GestureUtils"]

class GestureUtils(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/gesture/GestureUtils"
    spatialSampling = JavaMultipleMethod([("(Landroid/gesture/Gesture;I)[F", True, False), ("(Landroid/gesture/Gesture;IZ)[F", True, False)])
    temporalSampling = JavaStaticMethod("(Landroid/gesture/GestureStroke;I)[F")
    computeOrientedBoundingBox = JavaMultipleMethod([("(Ljava/util/ArrayList;)Landroid/gesture/OrientedBoundingBox;", True, False), ("([F)Landroid/gesture/OrientedBoundingBox;", True, False)])