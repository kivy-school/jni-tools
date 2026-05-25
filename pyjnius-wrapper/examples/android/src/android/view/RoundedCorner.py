from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["RoundedCorner"]

class RoundedCorner(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/view/RoundedCorner"
    __javaconstructor__ = [("(IIII)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    POSITION_BOTTOM_LEFT = JavaStaticField("I")
    POSITION_BOTTOM_RIGHT = JavaStaticField("I")
    POSITION_TOP_LEFT = JavaStaticField("I")
    POSITION_TOP_RIGHT = JavaStaticField("I")
    getPosition = JavaMethod("()I")
    getRadius = JavaMethod("()I")
    getCenter = JavaMethod("()Landroid/graphics/Point;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    toString = JavaMethod("()Ljava/lang/String;")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")