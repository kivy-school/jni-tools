from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Point"]

class Point(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/graphics/Point"
    __javaconstructor__ = [("(II)V", False), ("(Landroid/graphics/Point;)V", False), ("()V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    x = JavaField("I")
    y = JavaField("I")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    equals = JavaMultipleMethod([("(II)Z", False, False), ("(Ljava/lang/Object;)Z", False, False)])
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    offset = JavaMethod("(II)V")
    set = JavaMethod("(II)V")
    negate = JavaMethod("()V")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    readFromParcel = JavaMethod("(Landroid/os/Parcel;)V")
    describeContents = JavaMethod("()I")