from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["QuoteSpan"]

class QuoteSpan(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/text/style/QuoteSpan"
    __javaconstructor__ = [("()V", False), ("(Landroid/os/Parcel;)V", False), ("(I)V", False), ("(III)V", False)]
    STANDARD_COLOR = JavaStaticField("I")
    STANDARD_GAP_WIDTH_PX = JavaStaticField("I")
    STANDARD_STRIPE_WIDTH_PX = JavaStaticField("I")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    drawLeadingMargin = JavaMethod("(Landroid/graphics/Canvas;Landroid/graphics/Paint;IIIIILjava/lang/CharSequence;IIZLandroid/text/Layout;)V")
    getGapWidth = JavaMethod("()I")
    getLeadingMargin = JavaMethod("(Z)I")
    getStripeWidth = JavaMethod("()I")
    toString = JavaMethod("()Ljava/lang/String;")
    getColor = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")
    getSpanTypeId = JavaMethod("()I")