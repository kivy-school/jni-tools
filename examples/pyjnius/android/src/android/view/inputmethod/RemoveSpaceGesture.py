from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["RemoveSpaceGesture"]

class RemoveSpaceGesture(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/view/inputmethod/RemoveSpaceGesture"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    getStartPoint = JavaMethod("()Landroid/graphics/PointF;")
    getEndPoint = JavaMethod("()Landroid/graphics/PointF;")
    hashCode = JavaMethod("()I")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/view/inputmethod/RemoveSpaceGesture/Builder"
        __javaconstructor__ = [("()V", False)]
        setPoints = JavaMethod("(Landroid/graphics/PointF;Landroid/graphics/PointF;)Landroid/view/inputmethod/RemoveSpaceGesture$Builder;")
        setFallbackText = JavaMethod("(Ljava/lang/String;)Landroid/view/inputmethod/RemoveSpaceGesture$Builder;")
        build = JavaMethod("()Landroid/view/inputmethod/RemoveSpaceGesture;")