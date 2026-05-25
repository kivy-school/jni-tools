from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["PointF"]

class PointF(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/graphics/PointF"
    __javaconstructor__ = [("()V", False), ("(FF)V", False), ("(Landroid/graphics/Point;)V", False), ("(Landroid/graphics/PointF;)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    x = JavaField("F")
    y = JavaField("F")
    set = JavaMultipleMethod([("(FF)V", False, False), ("(Landroid/graphics/PointF;)V", False, False)])
    negate = JavaMethod("()V")
    offset = JavaMethod("(FF)V")
    equals = JavaMultipleMethod([("(FF)Z", False, False), ("(Ljava/lang/Object;)Z", False, False)])
    hashCode = JavaMethod("()I")
    toString = JavaMethod("()Ljava/lang/String;")
    length = JavaMultipleMethod([("()F", False, False), ("(FF)F", True, False)])
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    readFromParcel = JavaMethod("(Landroid/os/Parcel;)V")