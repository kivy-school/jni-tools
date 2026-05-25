from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["StyleSpan"]

class StyleSpan(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/text/style/StyleSpan"
    __javaconstructor__ = [("(I)V", False), ("(II)V", False), ("(Landroid/os/Parcel;)V", False)]
    getSpanTypeId = JavaMethod("()I")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    getStyle = JavaMethod("()I")
    getFontWeightAdjustment = JavaMethod("()I")
    updateDrawState = JavaMethod("(Landroid/text/TextPaint;)V")
    updateMeasureState = JavaMethod("(Landroid/text/TextPaint;)V")
    toString = JavaMethod("()Ljava/lang/String;")