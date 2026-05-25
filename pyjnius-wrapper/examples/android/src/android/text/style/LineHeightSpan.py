from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["LineHeightSpan"]

class LineHeightSpan(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "android/text/style/LineHeightSpan"
    chooseHeight = JavaMethod("(Ljava/lang/CharSequence;IIIILandroid/graphics/Paint$FontMetricsInt;)V")

    class Standard(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/text/style/LineHeightSpan/Standard"
        __javaconstructor__ = [("(I)V", False), ("(Landroid/os/Parcel;)V", False)]
        getHeight = JavaMethod("()I")
        getSpanTypeId = JavaMethod("()I")
        describeContents = JavaMethod("()I")
        writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
        chooseHeight = JavaMethod("(Ljava/lang/CharSequence;IIIILandroid/graphics/Paint$FontMetricsInt;)V")

    class WithDensity(JavaInterface, metaclass=MetaJavaClass):
        __javaclass__ = "android/text/style/LineHeightSpan/WithDensity"
        chooseHeight = JavaMethod("(Ljava/lang/CharSequence;IIIILandroid/graphics/Paint$FontMetricsInt;Landroid/text/TextPaint;)V")