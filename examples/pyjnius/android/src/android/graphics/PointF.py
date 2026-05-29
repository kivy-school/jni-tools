from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["PointF"]

class PointF(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/graphics/PointF"
    __javaconstructor__ = [("(FF)V", False), ("(Landroid/graphics/PointF;)V", False), ("(Landroid/graphics/Point;)V", False), ("()V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    x = JavaField("F")
    y = JavaField("F")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    equals = JavaMultipleMethod([("(FF)Z", False, False), ("(Ljava/lang/Object;)Z", False, False)])
    length = JavaMultipleMethod([("()F", False, False), ("(FF)F", True, False)])
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    offset = JavaMethod("(FF)V")
    set = JavaMultipleMethod([("(FF)V", False, False), ("(Landroid/graphics/PointF;)V", False, False)])
    negate = JavaMethod("()V")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    readFromParcel = JavaMethod("(Landroid/os/Parcel;)V")
    describeContents = JavaMethod("()I")