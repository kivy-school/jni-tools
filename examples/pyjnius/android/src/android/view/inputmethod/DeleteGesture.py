from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["DeleteGesture"]

class DeleteGesture(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/view/inputmethod/DeleteGesture"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    GRANULARITY_CHARACTER = JavaStaticField("I")
    GRANULARITY_WORD = JavaStaticField("I")
    getGranularity = JavaMethod("()I")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")
    getDeletionArea = JavaMethod("()Landroid/graphics/RectF;")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/view/inputmethod/DeleteGesture$Builder"
        __javaconstructor__ = [("()V", False)]
        setFallbackText = JavaMethod("(Ljava/lang/String;)Landroid/view/inputmethod/DeleteGesture$Builder;")
        setGranularity = JavaMethod("(I)Landroid/view/inputmethod/DeleteGesture$Builder;")
        build = JavaMethod("()Landroid/view/inputmethod/DeleteGesture;")
        setDeletionArea = JavaMethod("(Landroid/graphics/RectF;)Landroid/view/inputmethod/DeleteGesture$Builder;")