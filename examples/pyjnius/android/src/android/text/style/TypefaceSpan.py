from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["TypefaceSpan"]

class TypefaceSpan(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/text/style/TypefaceSpan"
    __javaconstructor__ = [("(Landroid/graphics/Typeface;)V", False), ("(Ljava/lang/String;)V", False), ("(Landroid/os/Parcel;)V", False)]
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    updateMeasureState = JavaMethod("(Landroid/text/TextPaint;)V")
    getFamily = JavaMethod("()Ljava/lang/String;")
    toString = JavaMethod("()Ljava/lang/String;")
    getTypeface = JavaMethod("()Landroid/graphics/Typeface;")
    updateDrawState = JavaMethod("(Landroid/text/TextPaint;)V")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")
    getSpanTypeId = JavaMethod("()I")