from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["RelativeSizeSpan"]

class RelativeSizeSpan(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/text/style/RelativeSizeSpan"
    __javaconstructor__ = [("(Landroid/os/Parcel;)V", False), ("(F)V", False)]
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    updateMeasureState = JavaMethod("(Landroid/text/TextPaint;)V")
    getSizeChange = JavaMethod("()F")
    toString = JavaMethod("()Ljava/lang/String;")
    updateDrawState = JavaMethod("(Landroid/text/TextPaint;)V")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")
    getSpanTypeId = JavaMethod("()I")