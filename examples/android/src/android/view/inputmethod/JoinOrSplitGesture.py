from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["JoinOrSplitGesture"]

class JoinOrSplitGesture(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/view/inputmethod/JoinOrSplitGesture"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    getJoinOrSplitPoint = JavaMethod("()Landroid/graphics/PointF;")
    hashCode = JavaMethod("()I")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/view/inputmethod/JoinOrSplitGesture/Builder"
        __javaconstructor__ = [("()V", False)]
        setJoinOrSplitPoint = JavaMethod("(Landroid/graphics/PointF;)Landroid/view/inputmethod/JoinOrSplitGesture$Builder;")
        setFallbackText = JavaMethod("(Ljava/lang/String;)Landroid/view/inputmethod/JoinOrSplitGesture$Builder;")
        build = JavaMethod("()Landroid/view/inputmethod/JoinOrSplitGesture;")