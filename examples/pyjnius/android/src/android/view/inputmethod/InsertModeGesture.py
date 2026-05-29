from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["InsertModeGesture"]

class InsertModeGesture(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/view/inputmethod/InsertModeGesture"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    GRANULARITY_CHARACTER = JavaStaticField("I")
    GRANULARITY_WORD = JavaStaticField("I")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")
    getInsertionPoint = JavaMethod("()Landroid/graphics/PointF;")
    getCancellationSignal = JavaMethod("()Landroid/os/CancellationSignal;")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/view/inputmethod/InsertModeGesture$Builder"
        __javaconstructor__ = [("()V", False)]
        setInsertionPoint = JavaMethod("(Landroid/graphics/PointF;)Landroid/view/inputmethod/InsertModeGesture$Builder;")
        setCancellationSignal = JavaMethod("(Landroid/os/CancellationSignal;)Landroid/view/inputmethod/InsertModeGesture$Builder;")
        setFallbackText = JavaMethod("(Ljava/lang/String;)Landroid/view/inputmethod/InsertModeGesture$Builder;")
        build = JavaMethod("()Landroid/view/inputmethod/InsertModeGesture;")