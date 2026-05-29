from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["LineBackgroundSpan"]

class LineBackgroundSpan(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/text/style/LineBackgroundSpan"
    drawBackground = JavaMethod("(Landroid/graphics/Canvas;Landroid/graphics/Paint;IIIIILjava/lang/CharSequence;III)V")

    class Standard(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/text/style/LineBackgroundSpan$Standard"
        __javaconstructor__ = [("(Landroid/os/Parcel;)V", False), ("(I)V", False)]
        CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
        PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
        getColor = JavaMethod("()I")
        drawBackground = JavaMethod("(Landroid/graphics/Canvas;Landroid/graphics/Paint;IIIIILjava/lang/CharSequence;III)V")
        writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
        describeContents = JavaMethod("()I")
        getSpanTypeId = JavaMethod("()I")