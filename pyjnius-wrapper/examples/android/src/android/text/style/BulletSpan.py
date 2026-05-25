from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["BulletSpan"]

class BulletSpan(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/text/style/BulletSpan"
    __javaconstructor__ = [("()V", False), ("(I)V", False), ("(II)V", False), ("(III)V", False), ("(Landroid/os/Parcel;)V", False)]
    STANDARD_GAP_WIDTH = JavaStaticField("I")
    getSpanTypeId = JavaMethod("()I")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    getLeadingMargin = JavaMethod("(Z)I")
    getGapWidth = JavaMethod("()I")
    getBulletRadius = JavaMethod("()I")
    getColor = JavaMethod("()I")
    drawLeadingMargin = JavaMethod("(Landroid/graphics/Canvas;Landroid/graphics/Paint;IIIIILjava/lang/CharSequence;IIZLandroid/text/Layout;)V")
    toString = JavaMethod("()Ljava/lang/String;")