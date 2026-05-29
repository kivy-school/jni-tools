from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["OrientedBoundingBox"]

class OrientedBoundingBox(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/gesture/OrientedBoundingBox"
    centerX = JavaField("F")
    centerY = JavaField("F")
    height = JavaField("F")
    orientation = JavaField("F")
    squareness = JavaField("F")
    width = JavaField("F")