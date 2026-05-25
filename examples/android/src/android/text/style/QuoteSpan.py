from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["QuoteSpan"]

class QuoteSpan(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/text/style/QuoteSpan"
    __javaconstructor__ = [("()V", False), ("(I)V", False), ("(III)V", False), ("(Landroid/os/Parcel;)V", False)]
    STANDARD_COLOR = JavaStaticField("I")
    STANDARD_GAP_WIDTH_PX = JavaStaticField("I")
    STANDARD_STRIPE_WIDTH_PX = JavaStaticField("I")
    getSpanTypeId = JavaMethod("()I")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    getColor = JavaMethod("()I")
    getStripeWidth = JavaMethod("()I")
    getGapWidth = JavaMethod("()I")
    getLeadingMargin = JavaMethod("(Z)I")
    drawLeadingMargin = JavaMethod("(Landroid/graphics/Canvas;Landroid/graphics/Paint;IIIIILjava/lang/CharSequence;IIZLandroid/text/Layout;)V")
    toString = JavaMethod("()Ljava/lang/String;")