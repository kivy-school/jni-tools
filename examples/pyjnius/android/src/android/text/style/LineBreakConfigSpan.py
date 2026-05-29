from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["LineBreakConfigSpan"]

class LineBreakConfigSpan(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/text/style/LineBreakConfigSpan"
    __javaconstructor__ = [("(Landroid/graphics/text/LineBreakConfig;)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    getLineBreakConfig = JavaMethod("()Landroid/graphics/text/LineBreakConfig;")
    createNoBreakSpan = JavaStaticMethod("()Landroid/text/style/LineBreakConfigSpan;")
    createNoHyphenationSpan = JavaStaticMethod("()Landroid/text/style/LineBreakConfigSpan;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    toString = JavaMethod("()Ljava/lang/String;")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    getSpanTypeId = JavaMethod("()I")