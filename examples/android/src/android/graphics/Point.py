from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Point"]

class Point(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/graphics/Point"
    __javaconstructor__ = [("()V", False), ("(II)V", False), ("(Landroid/graphics/Point;)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    x = JavaField("I")
    y = JavaField("I")
    set = JavaMethod("(II)V")
    negate = JavaMethod("()V")
    offset = JavaMethod("(II)V")
    equals = JavaMultipleMethod([("(II)Z", False, False), ("(Ljava/lang/Object;)Z", False, False)])
    hashCode = JavaMethod("()I")
    toString = JavaMethod("()Ljava/lang/String;")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    readFromParcel = JavaMethod("(Landroid/os/Parcel;)V")