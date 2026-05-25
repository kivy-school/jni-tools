from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["LeadingMarginSpan"]

class LeadingMarginSpan(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "android/text/style/LeadingMarginSpan"
    getLeadingMargin = JavaMethod("(Z)I")
    drawLeadingMargin = JavaMethod("(Landroid/graphics/Canvas;Landroid/graphics/Paint;IIIIILjava/lang/CharSequence;IIZLandroid/text/Layout;)V")

    class LeadingMarginSpan2(JavaInterface, metaclass=MetaJavaClass):
        __javaclass__ = "android/text/style/LeadingMarginSpan/LeadingMarginSpan2"
        getLeadingMarginLineCount = JavaMethod("()I")

    class Standard(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/text/style/LeadingMarginSpan/Standard"
        __javaconstructor__ = [("(II)V", False), ("(I)V", False), ("(Landroid/os/Parcel;)V", False)]
        getSpanTypeId = JavaMethod("()I")
        describeContents = JavaMethod("()I")
        writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
        getLeadingMargin = JavaMethod("(Z)I")
        drawLeadingMargin = JavaMethod("(Landroid/graphics/Canvas;Landroid/graphics/Paint;IIIIILjava/lang/CharSequence;IIZLandroid/text/Layout;)V")