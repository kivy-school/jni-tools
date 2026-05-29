from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["LineHeightSpan"]

class LineHeightSpan(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/text/style/LineHeightSpan"
    chooseHeight = JavaMethod("(Ljava/lang/CharSequence;IIIILandroid/graphics/Paint$FontMetricsInt;)V")

    class WithDensity(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/text/style/LineHeightSpan$WithDensity"
        chooseHeight = JavaMethod("(Ljava/lang/CharSequence;IIIILandroid/graphics/Paint$FontMetricsInt;Landroid/text/TextPaint;)V")

    class Standard(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/text/style/LineHeightSpan$Standard"
        __javaconstructor__ = [("(Landroid/os/Parcel;)V", False), ("(I)V", False)]
        CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
        PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
        chooseHeight = JavaMethod("(Ljava/lang/CharSequence;IIIILandroid/graphics/Paint$FontMetricsInt;)V")
        getHeight = JavaMethod("()I")
        writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
        describeContents = JavaMethod("()I")
        getSpanTypeId = JavaMethod("()I")