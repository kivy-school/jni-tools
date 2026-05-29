from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["TypefaceSpan"]

class TypefaceSpan(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/text/style/TypefaceSpan"
    __javaconstructor__ = [("(Ljava/lang/String;)V", False), ("(Landroid/graphics/Typeface;)V", False), ("(Landroid/os/Parcel;)V", False)]
    getSpanTypeId = JavaMethod("()I")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    getFamily = JavaMethod("()Ljava/lang/String;")
    getTypeface = JavaMethod("()Landroid/graphics/Typeface;")
    updateDrawState = JavaMethod("(Landroid/text/TextPaint;)V")
    updateMeasureState = JavaMethod("(Landroid/text/TextPaint;)V")
    toString = JavaMethod("()Ljava/lang/String;")