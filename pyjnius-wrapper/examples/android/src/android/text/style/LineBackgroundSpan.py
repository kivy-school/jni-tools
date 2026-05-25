from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["LineBackgroundSpan"]

class LineBackgroundSpan(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "android/text/style/LineBackgroundSpan"
    drawBackground = JavaMethod("(Landroid/graphics/Canvas;Landroid/graphics/Paint;IIIIILjava/lang/CharSequence;III)V")

    class Standard(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/text/style/LineBackgroundSpan/Standard"
        __javaconstructor__ = [("(I)V", False), ("(Landroid/os/Parcel;)V", False)]
        getSpanTypeId = JavaMethod("()I")
        describeContents = JavaMethod("()I")
        writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
        getColor = JavaMethod("()I")
        drawBackground = JavaMethod("(Landroid/graphics/Canvas;Landroid/graphics/Paint;IIIIILjava/lang/CharSequence;III)V")