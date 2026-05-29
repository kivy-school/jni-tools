from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["JoinOrSplitGesture"]

class JoinOrSplitGesture(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/view/inputmethod/JoinOrSplitGesture"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    GRANULARITY_CHARACTER = JavaStaticField("I")
    GRANULARITY_WORD = JavaStaticField("I")
    getJoinOrSplitPoint = JavaMethod("()Landroid/graphics/PointF;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/view/inputmethod/JoinOrSplitGesture$Builder"
        __javaconstructor__ = [("()V", False)]
        setJoinOrSplitPoint = JavaMethod("(Landroid/graphics/PointF;)Landroid/view/inputmethod/JoinOrSplitGesture$Builder;")
        setFallbackText = JavaMethod("(Ljava/lang/String;)Landroid/view/inputmethod/JoinOrSplitGesture$Builder;")
        build = JavaMethod("()Landroid/view/inputmethod/JoinOrSplitGesture;")