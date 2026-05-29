from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AbsoluteSizeSpan"]

class AbsoluteSizeSpan(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/text/style/AbsoluteSizeSpan"
    __javaconstructor__ = [("(Landroid/os/Parcel;)V", False), ("(IZ)V", False), ("(I)V", False)]
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    getDip = JavaMethod("()Z")
    updateMeasureState = JavaMethod("(Landroid/text/TextPaint;)V")
    toString = JavaMethod("()Ljava/lang/String;")
    getSize = JavaMethod("()I")
    updateDrawState = JavaMethod("(Landroid/text/TextPaint;)V")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")
    getSpanTypeId = JavaMethod("()I")