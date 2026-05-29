from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["StyleSpan"]

class StyleSpan(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/text/style/StyleSpan"
    __javaconstructor__ = [("(Landroid/os/Parcel;)V", False), ("(II)V", False), ("(I)V", False)]
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    updateMeasureState = JavaMethod("(Landroid/text/TextPaint;)V")
    getFontWeightAdjustment = JavaMethod("()I")
    toString = JavaMethod("()Ljava/lang/String;")
    getStyle = JavaMethod("()I")
    updateDrawState = JavaMethod("(Landroid/text/TextPaint;)V")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")
    getSpanTypeId = JavaMethod("()I")