from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SelectGesture"]

class SelectGesture(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/view/inputmethod/SelectGesture"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    getGranularity = JavaMethod("()I")
    getSelectionArea = JavaMethod("()Landroid/graphics/RectF;")
    hashCode = JavaMethod("()I")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/view/inputmethod/SelectGesture/Builder"
        __javaconstructor__ = [("()V", False)]
        setGranularity = JavaMethod("(I)Landroid/view/inputmethod/SelectGesture$Builder;")
        setSelectionArea = JavaMethod("(Landroid/graphics/RectF;)Landroid/view/inputmethod/SelectGesture$Builder;")
        setFallbackText = JavaMethod("(Ljava/lang/String;)Landroid/view/inputmethod/SelectGesture$Builder;")
        build = JavaMethod("()Landroid/view/inputmethod/SelectGesture;")