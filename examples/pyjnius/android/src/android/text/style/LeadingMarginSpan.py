from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["LeadingMarginSpan"]

class LeadingMarginSpan(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/text/style/LeadingMarginSpan"
    drawLeadingMargin = JavaMethod("(Landroid/graphics/Canvas;Landroid/graphics/Paint;IIIIILjava/lang/CharSequence;IIZLandroid/text/Layout;)V")
    getLeadingMargin = JavaMethod("(Z)I")

    class Standard(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/text/style/LeadingMarginSpan$Standard"
        __javaconstructor__ = [("(Landroid/os/Parcel;)V", False), ("(I)V", False), ("(II)V", False)]
        CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
        PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
        drawLeadingMargin = JavaMethod("(Landroid/graphics/Canvas;Landroid/graphics/Paint;IIIIILjava/lang/CharSequence;IIZLandroid/text/Layout;)V")
        getLeadingMargin = JavaMethod("(Z)I")
        writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
        describeContents = JavaMethod("()I")
        getSpanTypeId = JavaMethod("()I")

    class LeadingMarginSpan2(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/text/style/LeadingMarginSpan$LeadingMarginSpan2"
        getLeadingMarginLineCount = JavaMethod("()I")