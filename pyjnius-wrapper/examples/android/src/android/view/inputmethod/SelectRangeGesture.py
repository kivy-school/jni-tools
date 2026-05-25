from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SelectRangeGesture"]

class SelectRangeGesture(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/view/inputmethod/SelectRangeGesture"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    getGranularity = JavaMethod("()I")
    getSelectionStartArea = JavaMethod("()Landroid/graphics/RectF;")
    getSelectionEndArea = JavaMethod("()Landroid/graphics/RectF;")
    hashCode = JavaMethod("()I")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/view/inputmethod/SelectRangeGesture/Builder"
        __javaconstructor__ = [("()V", False)]
        setGranularity = JavaMethod("(I)Landroid/view/inputmethod/SelectRangeGesture$Builder;")
        setSelectionStartArea = JavaMethod("(Landroid/graphics/RectF;)Landroid/view/inputmethod/SelectRangeGesture$Builder;")
        setSelectionEndArea = JavaMethod("(Landroid/graphics/RectF;)Landroid/view/inputmethod/SelectRangeGesture$Builder;")
        setFallbackText = JavaMethod("(Ljava/lang/String;)Landroid/view/inputmethod/SelectRangeGesture$Builder;")
        build = JavaMethod("()Landroid/view/inputmethod/SelectRangeGesture;")