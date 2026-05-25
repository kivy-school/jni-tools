from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["InsertModeGesture"]

class InsertModeGesture(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/view/inputmethod/InsertModeGesture"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    getCancellationSignal = JavaMethod("()Landroid/os/CancellationSignal;")
    getInsertionPoint = JavaMethod("()Landroid/graphics/PointF;")
    hashCode = JavaMethod("()I")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/view/inputmethod/InsertModeGesture/Builder"
        __javaconstructor__ = [("()V", False)]
        setInsertionPoint = JavaMethod("(Landroid/graphics/PointF;)Landroid/view/inputmethod/InsertModeGesture$Builder;")
        setCancellationSignal = JavaMethod("(Landroid/os/CancellationSignal;)Landroid/view/inputmethod/InsertModeGesture$Builder;")
        setFallbackText = JavaMethod("(Ljava/lang/String;)Landroid/view/inputmethod/InsertModeGesture$Builder;")
        build = JavaMethod("()Landroid/view/inputmethod/InsertModeGesture;")