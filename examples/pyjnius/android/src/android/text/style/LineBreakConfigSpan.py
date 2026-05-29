from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["LineBreakConfigSpan"]

class LineBreakConfigSpan(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/text/style/LineBreakConfigSpan"
    __javaconstructor__ = [("(Landroid/graphics/text/LineBreakConfig;)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    createNoBreakSpan = JavaStaticMethod("()Landroid/text/style/LineBreakConfigSpan;")
    createNoHyphenationSpan = JavaStaticMethod("()Landroid/text/style/LineBreakConfigSpan;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    getLineBreakConfig = JavaMethod("()Landroid/graphics/text/LineBreakConfig;")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")
    getSpanTypeId = JavaMethod("()I")