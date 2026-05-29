from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["InsertGesture"]

class InsertGesture(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/view/inputmethod/InsertGesture"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    GRANULARITY_CHARACTER = JavaStaticField("I")
    GRANULARITY_WORD = JavaStaticField("I")
    getTextToInsert = JavaMethod("()Ljava/lang/String;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")
    getInsertionPoint = JavaMethod("()Landroid/graphics/PointF;")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/view/inputmethod/InsertGesture$Builder"
        __javaconstructor__ = [("()V", False)]
        setInsertionPoint = JavaMethod("(Landroid/graphics/PointF;)Landroid/view/inputmethod/InsertGesture$Builder;")
        setFallbackText = JavaMethod("(Ljava/lang/String;)Landroid/view/inputmethod/InsertGesture$Builder;")
        setTextToInsert = JavaMethod("(Ljava/lang/String;)Landroid/view/inputmethod/InsertGesture$Builder;")
        build = JavaMethod("()Landroid/view/inputmethod/InsertGesture;")