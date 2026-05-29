from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["RemoveSpaceGesture"]

class RemoveSpaceGesture(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/view/inputmethod/RemoveSpaceGesture"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    GRANULARITY_CHARACTER = JavaStaticField("I")
    GRANULARITY_WORD = JavaStaticField("I")
    getEndPoint = JavaMethod("()Landroid/graphics/PointF;")
    getStartPoint = JavaMethod("()Landroid/graphics/PointF;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/view/inputmethod/RemoveSpaceGesture$Builder"
        __javaconstructor__ = [("()V", False)]
        setFallbackText = JavaMethod("(Ljava/lang/String;)Landroid/view/inputmethod/RemoveSpaceGesture$Builder;")
        setPoints = JavaMethod("(Landroid/graphics/PointF;Landroid/graphics/PointF;)Landroid/view/inputmethod/RemoveSpaceGesture$Builder;")
        build = JavaMethod("()Landroid/view/inputmethod/RemoveSpaceGesture;")